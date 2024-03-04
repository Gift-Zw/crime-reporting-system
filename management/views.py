import threading

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control

from core.models import CrimeReport, CrimeAttachment, AnonymousReport, AnonymousAttachment, WantedPerson, PoliceStation, \
    CrimeReportComment
from .forms import PoliceStationForm, WantedPersonForm, EditCreateReportForm, EditAnonymousReportForm, CommentForm
from .decorators import admin_required
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.core.mail import EmailMessage
from auditlog.models import LogEntry


class EmailThread(threading.Thread):
    def __init__(self, email):
        super().__init__()
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)


def custom_send_email(report: CrimeReport, new_status, old_status):
    subject = f"Subject: Update on Your Crime Report: {report.id}"
    to_email = ["{}".format(report.reporter.email)]
    email_message = f"""
    Dear {report.reporter.full_name},
    We hope this email finds you well. We wanted to provide you with an update regarding the status of your recent crime report ({0}). Our team has been diligently investigating the matter, and we are pleased to inform you that there has been progress in the case.
    The status of your report has been updated to: {new_status} from {old_status}
    We understand that this process can be stressful, and we appreciate your patience and cooperation throughout the investigation. Please be assured that we are committed to resolving this matter thoroughly and efficiently.
    If you have any questions or need further assistance, please don't hesitate to contact us.
    Best regards,
    """
    email = EmailMessage(
        subject=subject,
        to=to_email,
        body=email_message,
        from_email='gift200161@gmail.com'
    )
    # Start the email thread
    EmailThread(email=email).start()


# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def management_logout_view(request):
    logout(request)
    return redirect('management-login')


class AdminLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'management/admin_login.html'
    redirect_authenticated_user = True
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy('management-dashboard')


@admin_required
def dashboard_view(request):
    context = {
        'reports': CrimeReport.objects.all()
    }
    return render(request, 'management/index.html', context)


@admin_required
def anonymous_reports_view(request):
    context = {
        'reports': AnonymousReport.objects.all()
    }
    return render(request, 'management/anonymous_report.html', context)


@admin_required
def crime_reports_view(request):
    context = {
        'reports': CrimeReport.objects.all()
    }
    return render(request, 'management/crime_reports.html', context)


@admin_required
def logs_view(request):
    context = {
        'logs' : LogEntry.objects.all()
    }
    return render(request, 'management/logs.html', context)


@admin_required
def police_stations_view(request):
    if request.method == 'POST':
        form = PoliceStationForm(request.POST)
        if form.is_valid():
            station = PoliceStation.objects.create(
                name=form.data['name'],
                phone=form.data['phone'],
                location=form.data['location'],
                city=form.data['city'],
                latitude=form.data['latitude'],
                longitude=form.data['longitude']
            )
            station.save()
            messages.success(request, 'The police station has been successfully added')
            return redirect('management-police-stations')
        else:
            messages.error(request, form.errors)

    else:
        form = PoliceStationForm()
    context = {
        'police_stations': PoliceStation.objects.all(),
        'form': PoliceStationForm()
    }
    return render(request, 'management/police_stations.html', context)


@admin_required
def wanted_persons_view(request):
    if request.method == 'POST':
        form = WantedPersonForm(request.POST)
        if form.is_valid():
            person = WantedPerson.objects.create(
                name=form.data['name'], alias=form.data['alias'],
                gender=form.data['gender'],last_known_location=form.data['last_known_location'],
                offense=form.data['offense'],contact_info=form.data['contact_info']
            )
            person.save()
            messages.success(request, 'The wanted person has been successfully added')
            return redirect('management-wanted-persons')
        else:
            messages.error(request, form.errors)
    else:
        form = WantedPersonForm()
    context = {
        'wanted_persons': WantedPerson.objects.all(),
        'form': WantedPersonForm
    }
    return render(request, 'management/wanted_persons.html', context)


@admin_required
def crime_report_detail_view(request, id):
    report = CrimeReport.objects.get(id=id)
    files = CrimeAttachment.objects.filter(crime=report)
    comments = CrimeReportComment.objects.filter(report=report)
    number_of_comments = comments.count()
    if request.method == 'POST':
        if 'status' in request.POST:
            form = EditCreateReportForm(request.POST)
            if form.is_valid():
                if form.data['status'] != '':
                    if report.status != form.data['status']:
                        custom_send_email(report, form.data['status'], report.status)
                        report.status = form.data['status']
                        report.save()

                if len(str(form.data['assigned_officer'])) > 0:
                    officer = User.objects.get(id=int(form.data['assigned_officer']))
                    report.assigned_officer = officer
                    report.save()

                messages.success(request, 'The crime report has been successfully edited')
                return redirect('management-report-detail', report.id)
            else:
                messages.error(request, form.errors)

        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = CrimeReportComment.objects.create(
                    report=report,
                    user=request.user,
                    comment=comment_form.data['post_comment'],
                )
                comment.save()
                return redirect('management-report-detail', report.id)
            else:
                return redirect('management-report-detail', report.id)

    else:
        form = EditCreateReportForm()
        comment_form = CommentForm()

    context = {
        'report': report,
        'files': files,
        'form': EditCreateReportForm(),
        'comment_form': CommentForm(),
        'comments': comments,
        'comments_number':number_of_comments
    }
    return render(request, 'management/report_details.html', context)

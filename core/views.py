from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control
from django.views.generic import CreateView

from .forms import CreateReportForm, CreateAnonymousReportForm
from .models import CrimeReport, CrimeAttachment, AnonymousReport, AnonymousAttachment, PoliceStation, WantedPerson
from .decorators import citizen_required
from django.contrib.auth.forms import AuthenticationForm
from management.models import User
from management.admin import UserCreationForm


# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_logout_view(request):
    logout(request)
    return redirect('user-login')


class UserRegistrationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('user-police-stations')

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = User.objects.get(email=email)
        login(self.request, user)
        return redirect('user-dashboard')


class RegularUserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/user_login.html'
    redirect_authenticated_user = True
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy('user-dashboard')


@citizen_required
def dashboard_view(request):
    context = {}
    return render(request, 'users/dashboard.html', context)


@citizen_required
def my_reports_view(request):
    context = {
        'reports': CrimeReport.objects.filter(reporter=request.user)
    }
    return render(request, 'users/my_reports.html', context)


@citizen_required
def wanted_persons_view(request):
    context = {
        'wanted_persons': WantedPerson.objects.all()
    }
    return render(request, 'users/wanted_people.html', context)


@citizen_required
def police_stations_view(request):
    context = {
        'stations': PoliceStation.objects.all()
    }
    return render(request, 'users/police_stations.html', context)


@citizen_required
def create_crime_report_view(request):
    if request.method == 'POST':
        form = CreateReportForm(request.POST)
        files = request.FILES.getlist('files')
        if form.is_valid():
            report = CrimeReport.objects.create(
                crime_type=form.data['crime_type'],
                location=form.data['location'],
                city=form.data['city'],
                suspect_information=form.data['suspect_information'],
                witness_information=form.data['suspect_information'],
                reporter_cell=form.data['reporter_cell'],
                date=form.data['date'],
                description=form.data['description'],
                reporter=request.user
            )
            report.save()
            for file in files:
                file = CrimeAttachment.objects.create(
                    crime=report,
                    file=file
                )
                file.save()
            return redirect('user-reports')
        else:
            messages.error(request, form.errors)
    else:
        form = CreateReportForm()
    context = {
        'form': form,
    }

    return render(request, 'users/create_crime_report.html', context)


@citizen_required
def create_anonymous_report_view(request):
    if request.method == 'POST':
        form = CreateAnonymousReportForm(request.POST)
        files = request.FILES.getlist('files')
        if form.is_valid():
            report = AnonymousReport.objects.create(
                crime_type=form.data['crime_type'],
                location=form.data['location'],
                city=form.data['city'],
                suspect_information=form.data['suspect_information'],
                witness_information=form.data['suspect_information'],
                date=form.data['date'],
                description=form.data['description'],
            )
            report.save()
            for file in files:
                file = CrimeAttachment.objects.create(
                    crime=report,
                    file=file
                )
                file.save()
            return redirect('user-reports')
    else:
        form = CreateAnonymousReportForm()
    context = {
        'form': form,
    }

    return render(request, 'users/create_anonymous_report.html', context)


@citizen_required
def crime_report_detail_view(request, id):
    report = CrimeReport.objects.get(id=id)
    files = CrimeAttachment.objects.filter(crime=report)

    context = {
        'report': report,
        'files': files,
    }
    return render(request, 'users/user-report-detail.html', context)

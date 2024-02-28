from django.test import TestCase, Client
from core.models import CrimeReport
from core.forms import CreateReportForm
from core.views import create_crime_report_view


class CrimeReportModelTestCase(TestCase):
    def test_create_crime_report(self):
        # Create a new CrimeReport object
        report = CrimeReport.objects.create(title='Test Crime Report', description='This is a test report.')
        # Retrieve the created report from the database
        retrieved_report = CrimeReport.objects.get(title='Test Crime Report')
        # Assert that the retrieved report matches the created report
        self.assertEqual(report, retrieved_report)


class CrimeReportFormTestCase(TestCase):
    def test_crime_report_form_validation(self):
        # Create form data with invalid input
        form_data = {'title': '', 'description': ''}
        # Create form instance with form data
        form = CreateReportForm(data=form_data)
        # Assert that the form is not valid
        self.assertFalse(form.is_valid())


class CrimeReportViewTestCase(TestCase):
    def test_crime_report_view(self):
        # Create a testing client
        client = Client()
        # Send a GET request to the CrimeReportView
        response = client.get('/crime-report/')
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'crime_report.html')
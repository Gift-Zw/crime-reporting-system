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


from django.test import TestCase
from django.urls import reverse


class CitizenManagementIntegrationTestCase(TestCase):
    def test_citizen_report_updates_management_view(self):
        # Create a citizen crime report
        report = CrimeReport.objects.create(title='Test Crime Report', description='This is a test report.')
        # Send a POST request to the Management app to update the report status
        response = self.client.post(reverse('management:update_report_status', args=[report.id]),
                                    {'status': 'In Progress'})
        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Retrieve the updated report from the database
        updated_report = CrimeReport.objects.get(id=report.id)
        # Assert that the report status is updated correctly
        self.assertEqual(updated_report.status, 'In Progress')


from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AuthenticationIntegrationTestCase(TestCase):
    def test_citizen_login(self):
        # Create a citizen user
        user = User.objects.create_user(username='citizen', password='password')
        # Log in as the citizen user
        self.client.login(username='citizen', password='password')
        # Send a GET request to a citizen-specific page
        response = self.client.get(reverse('citizen:crime_report_list'))
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)


from django.test import TestCase
from .blockchain import EthereumClient


class BlockchainIntegrationTestCase(TestCase):
    def test_store_crime_record_on_blockchain(self):
        # Create a new crime record
        record_data = {'title': 'Test Crime Record', 'description': 'This is a test record.'}
        # Store the record on the blockchain
        ethereum_client = EthereumClient()
        transaction_id = ethereum_client.store_crime_record(record_data)
        # Check if the transaction was successful
        self.assertIsNotNone(transaction_id)

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from management.models import User
from auditlog.registry import auditlog


class AnonymousReport(models.Model):
    crime_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    date = models.DateTimeField()
    suspect_information = models.CharField(max_length=255, default='N/A')
    description = models.TextField()
    status = models.CharField(max_length=255, default='Received')
    assigned_officer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='officer',
                                         default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.crime_type


class AnonymousAttachment(models.Model):
    crime = models.ForeignKey(AnonymousReport, on_delete=models.CASCADE)
    file = models.FileField(upload_to='anonymous')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crime.crime_type


class CrimeReport(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')
    crime_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    date = models.DateTimeField()
    suspect_information = models.CharField(max_length=255, default='N/A')
    witness_information = models.CharField(max_length=255, default='N/A')
    reporter_cell = models.CharField(max_length=25, default='N/A')
    description = models.TextField(default='N/A')
    status = models.CharField(max_length=255, default='Under Review')
    assigned_officer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='assigned_officer',
                                         default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'CrimeID : {self.id}'


class CrimeAttachment(models.Model):
    crime = models.ForeignKey(CrimeReport, on_delete=models.CASCADE)
    file = models.FileField(upload_to='crime report')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crime.crime_type


class CrimeReportComment(models.Model):
    report = models.ForeignKey(CrimeReport, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=700)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.full_name


class PoliceStation(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=5)
    longitude = models.DecimalField(max_digits=10, decimal_places=5)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WantedPerson(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    last_known_location = models.CharField(max_length=255)
    offense = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=25)
    image = models.ImageField(upload_to='wanted', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


auditlog.register(WantedPerson)
auditlog.register(PoliceStation)
auditlog.register(CrimeReport)
auditlog.register(CrimeAttachment)
auditlog.register(CrimeReportComment)
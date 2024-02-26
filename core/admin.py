from django.contrib import admin
from .models import AnonymousReport, AnonymousAttachment, CrimeReport, CrimeAttachment, PoliceStation, WantedPerson


class AnonymousReportAdmin(admin.ModelAdmin):
    list_display = ['crime_type', 'location', 'city', 'date', 'suspect_information', 'description', 'status',
                    'assigned_officer', 'date_created', 'last_modified']


class AnonymousAttachmentAdmin(admin.ModelAdmin):
    list_display = ['crime', 'file', 'date_created']


class CrimeReportAdmin(admin.ModelAdmin):
    list_display = ['reporter', 'crime_type', 'location', 'city', 'date', 'suspect_information', 'witness_information',
                    'reporter_cell', 'description', 'status', 'assigned_officer', 'date_created', 'last_modified']


class CrimeAttachmentAdmin(admin.ModelAdmin):
    list_display = ['crime', 'file', 'date_created']


class PoliceStationAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'city', 'phone', 'latitude', 'longitude', 'date_created', 'last_modified']


class WantedPersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias', 'gender', 'last_known_location', 'offense', 'contact_info', 'image',
                    'date_added', 'last_modified']


# Register your models with the customized admin classes
admin.site.register(AnonymousReport, AnonymousReportAdmin)
admin.site.register(AnonymousAttachment, AnonymousAttachmentAdmin)
admin.site.register(CrimeReport, CrimeReportAdmin)
admin.site.register(CrimeAttachment, CrimeAttachmentAdmin)
admin.site.register(PoliceStation, PoliceStationAdmin)
admin.site.register(WantedPerson, WantedPersonAdmin)

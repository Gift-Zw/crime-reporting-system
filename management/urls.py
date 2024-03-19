from django.contrib import admin
from django.urls import path
from .views import dashboard_view, police_stations_view, logs_view, anonymous_reports_view, wanted_persons_view, \
    crime_reports_view, AdminLoginView, management_logout_view, crime_report_detail_view, assigned_crime_reports_view

urlpatterns = [
    path('dashboard/', dashboard_view, name="management-dashboard"),
    path('police-stations/', police_stations_view, name="management-police-stations"),
    path('logs/', logs_view, name="management-logs"),
    path('anonymous-reports/', anonymous_reports_view, name="management-anonymous-reports"),
    path('crime-reports/', crime_reports_view, name="management-crime-reports"),
    path('assigned-reports/', assigned_crime_reports_view, name="management-assigned-reports"),
    path('report-detail/<int:id>/', crime_report_detail_view, name="management-report-detail"),
    path('wanted-persons/', wanted_persons_view, name="management-wanted-persons"),
    path('log-in/', AdminLoginView.as_view(), name="management-login"),
    path('logout/', management_logout_view, name="management-logout"),
]

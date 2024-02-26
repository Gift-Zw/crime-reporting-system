from django.contrib import admin
from django.urls import path
from .views import dashboard_view, police_stations_view, my_reports_view, wanted_persons_view, create_crime_report_view, \
    create_anonymous_report_view, RegularUserLoginView, UserRegistrationView, user_logout_view, crime_report_detail_view

urlpatterns = [
    path('dashboard/', dashboard_view, name="user-dashboard"),
    path('police-stations/', police_stations_view, name="user-police-stations"),
    path('my-reports/', my_reports_view, name="user-reports"),
    path('wanted-persons/', wanted_persons_view, name="user-wanted-persons"),
    path('create-crime-report/', create_crime_report_view, name="user-create-report"),
    path('create-anonymous-report/', create_anonymous_report_view, name="user-create-anonymous"),
    path('log-in/', RegularUserLoginView.as_view(), name="user-login"),
    path('register/', UserRegistrationView.as_view(), name="user-register"),
    path('logout/', user_logout_view, name="user-logout"),
    path('crime-detail/<int:id>/', crime_report_detail_view, name="user-crime-detail"),
]

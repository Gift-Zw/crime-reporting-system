from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import localtime

CRIME_TYPES = (
    ('THEFT', 'Theft'),
    ('VANDALISM', 'Vandalism'),
    ('ASSAULT', 'Assault'),
    ('BURGLARY', 'Burglary'),
    ('ROBBERY', 'Robbery'),
    ('FRAUD', 'Fraud'),
    ('DRUG_OFFENSE', 'Drug Offense'),
    ('KIDNAPPING', 'Kidnapping'),

)


def validate_date_not_in_future(value):
    if value > localtime().date():
        raise ValidationError("Date cannot be in the future")


class CreateReportForm(forms.Form):
    crime_type = forms.CharField(widget=forms.Select(attrs={'class': 'form-control', }, choices=CRIME_TYPES))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    suspect_information = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    witness_information = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    reporter_cell = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    date = forms.DateField(validators=[validate_date_not_in_future], widget=forms.TextInput(attrs=(
        {'class': "form-control", 'id': "example-date", 'type': "date", 'name': "date"})))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3 }))


class CreateAnonymousReportForm(forms.Form):
    crime_type = forms.CharField(widget=forms.Select(attrs={'class': 'form-control', }, choices=CRIME_TYPES))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    suspect_information = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    witness_information = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }), required=False)
    date = forms.DateField(validators=[validate_date_not_in_future], widget=forms.TextInput(attrs=(
        {'class': "form-control", 'id': "example-date", 'type': "date", 'name': "date"})))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3}))


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':2 }))



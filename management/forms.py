from django import forms
from .models import User

CRIME_STATUS = (
    ('', ''),
    ('Under Review', 'Under Review'),
    ('Closed', 'Closed'),
    ('Under Investigation', 'Under Investigation'),
    ('Referred to Court', 'Referred to Court'),
    ('Suspended', 'Suspended'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class CommentForm(forms.Form):
    post_comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))


class PoliceStationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    latitude = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', }))
    longitude = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', }))


class WantedPersonForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    alias = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    gender = forms.CharField(widget=forms.Select(attrs={'class': 'form-control', }, choices=GENDER))
    last_known_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    offense = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    contact_info = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))


class EditCreateReportForm(forms.Form):
    status = forms.CharField(initial='', widget=forms.Select({'class': 'form-control', }, choices=CRIME_STATUS, ),
                             required=False)
    assigned_officer = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control', }),
                                              queryset=User.objects.filter(is_admin=True).order_by('first_name'),
                                              empty_label='Unassigned', required=False,
                                              initial='Unassigned')


class EditAnonymousReportForm(forms.Form):
    status = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', }))
    assigned_officer = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control', }),
                                              queryset=User.objects.filter(is_admin=True).order_by('first_name'),
                                              empty_label='Unassigned', required=False,
                                              initial='Unassigned')

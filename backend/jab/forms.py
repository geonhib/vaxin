from django import forms
from django.conf import settings
User=settings.AUTH_USER_MODEL
from django.forms import ModelForm, DateInput
from .models import Facility, Manufacturer, Vaccine, Vaccination
from django.forms import Form, ModelForm, DateField, widgets
import datetime


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = '__all__'
        exclude = ('active',)


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'
        exclude = ('approved',)


class VaccineForm(forms.ModelForm):
    def clean_date(self):
        date = self.cleaned_data['date']
        if self.expiry < datetime.date.today():
            raise forms.ValidationError("Expiry date cannot be in the past!")
        return date

    class Meta:
        model = Vaccine
        fields = '__all__'
        exclude = ('approved',)   
        widgets = {
            'expiry': widgets.DateInput(attrs={'type': 'date'})
        }     


class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = '__all__'
        exclude = ('approved', 'jabbed_by', 'jabbed_on')
        widgets = {
            'next_dose': widgets.DateInput(attrs={'type': 'date'})
        }


# class NextVaccinationForm(forms.ModelForm):
#     class Meta:
#         model = NextVaccination
#         fields = '__all__'
#         exclude = ('approved', 'drug', 'init_vaccination', 'jabbed_by', 'jabbed_on', )
#         widgets = {
#             'next_dose': widgets.DateInput(attrs={'type': 'date'})
#         }
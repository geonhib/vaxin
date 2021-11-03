from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, DateInput
from .models import Facility, Manufacturer, Vaccine, Vaccination
from django.forms import Form, ModelForm, DateField, widgets
import datetime


class FacilityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FacilityForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name of health facility"
        self.fields['center_level'].label = "Health facility center Level"
        self.fields['contact'].label = "Health facility contact details"
    class Meta:
        model = Facility
        fields = '__all__'
        exclude = ('active',)


class ManufacturerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ManufacturerForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name of drug manfacturer"
    class Meta:
        model = Manufacturer
        fields = '__all__'
        exclude = ('approved',)


class VaccineForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.filter(approved=True), empty_label='Select list of approved manufacturers')

    def __init__(self, *args, **kwargs):
        super(VaccineForm, self).__init__(*args, **kwargs)
        self.fields['batch'].label = "Batch number"
        self.fields['serial'].label = "Serial number"
        self.fields['name'].label = "Name of Vaccine"
        self.fields['doses'].label = "Number of doses to be administered"

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
    patient = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='Select from the list of patients')
    drug = forms.ModelChoiceField(queryset=Vaccine.objects.filter(approved=True), empty_label='Select from the list of approved drugs')
    jabbed_at = forms.ModelChoiceField(queryset=Facility.objects.all(), empty_label='Select from the list of health facilities')

    def __init__(self, *args, **kwargs):
        super(VaccinationForm, self).__init__(*args, **kwargs)
        self.fields['jabbed_at'].label = "Administered at"

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
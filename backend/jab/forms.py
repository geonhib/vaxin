from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, DateInput
from .models import Facility, Manufacturer, Vaccine, Batch, Vaccination, NextVaccination
from django.forms import Form, ModelForm, DateField, widgets
import datetime


class FacilityForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter health facility name'}))
    address = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter address of health facility'}))
    contact = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter contact details of health facility'}))

    def __init__(self, *args, **kwargs):
        super(FacilityForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Health facility"
        self.fields['name'].placeholder = "Health facility"
        self.fields['center_level'].label = "Health facility center Level"
        self.fields['contact'].label = "Health facility contact details"
    class Meta:
        model = Facility
        fields = '__all__'
        exclude = ('active',)


class ManufacturerForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter drug manufacturer '}))
    address = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter address of manufacturer'}))
    contact = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter contact of manufacturer'}))

    def __init__(self, *args, **kwargs):
        super(ManufacturerForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Drug manfacturer"
    class Meta:
        model = Manufacturer
        fields = '__all__'
        exclude = ('approved',)


class VaccineForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter name of drug'}))    
    batch = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter batch number of drug'}))
    serial = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter serial number of drug'}))
    doses = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter number of doses that should be administered'}))
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


class BatchForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter name of drug'}))    
    batch = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter batch number of drug'}))
    serial = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter serial number of drug'}))
    doses = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter number of doses that should be administered'}))
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.filter(approved=True), empty_label='Select list of approved manufacturers')

    def __init__(self, *args, **kwargs):
        super(BatchForm, self).__init__(*args, **kwargs)
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
        model = Batch
        fields = '__all__'
        exclude = ('approved',)   
        widgets = {
            'expiry': widgets.DateInput(attrs={'type': 'date'})
        } 


class VaccinationForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='Select from the list of patients')
    drug = forms.ModelChoiceField(queryset=Vaccine.objects.filter(approved=True), empty_label='Select from the list of approved vaccines')
    jabbed_at = forms.ModelChoiceField(queryset=Facility.objects.all(), empty_label='Select from the list of health facilities')

    def __init__(self, *args, **kwargs):
        super(VaccinationForm, self).__init__(*args, **kwargs)
        self.fields['jabbed_at'].label = "Administered at"
        

    class Meta:
        model = Vaccination
        fields = '__all__'
        exclude = ('approved', 'dose', 'jabbed_by', 'jabbed_on')
        widgets = {
            'next_dose': widgets.DateInput(attrs={'type': 'date'})
        }


class NextVaccinationForm(forms.ModelForm):
    jabbed_at = forms.ModelChoiceField(queryset=Facility.objects.all(), empty_label='Select health facilities dose was administered at')
    drug = forms.ModelChoiceField(queryset=Vaccine.objects.all(), empty_label='Select drug to be administered')

    def __init__(self, *args, **kwargs):
        super(NextVaccinationForm, self).__init__(*args, **kwargs)
        self.fields['jabbed_at'].label = "Dose taken from"
        self.fields['dose'].label = "Dose is complete"

    class Meta:
        model = NextVaccination
        fields = '__all__'
        exclude = ('approved', 'init_vaccination', 'jabbed_by', 'jabbed_on', )
        widgets = {
            'next_dose': widgets.DateInput(attrs={'type': 'date'}),
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import widgets
import datetime


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class UserForm(forms.ModelForm):
    telephone = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter telephone number.'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter your first name '}))   
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter your last name'})) 
    # gender = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Select your gender.'}))

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['gender'].placeholder = "Select gender"

    def clean_date(self):
        date = self.cleaned_data['date']
        if self.dob > datetime.date.today():
            raise forms.ValidationError("You birthdate cannot be in the future!")
        return date
  
    class Meta:
        model = User
        fields = ('telephone', 'first_name', 'last_name', 'gender', 'dob')
        exclude = ('username','password', 'date_joined', 'last_login', 'email', 'is_staff', 'is_superuser', 
       'groups', 'user_permissions', 'is_active', )
        widgets = {
            'dob': widgets.DateInput(attrs={'type': 'date'}),
            }
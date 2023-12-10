from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import Resume

# Registration
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Login

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Trans-Gender', 'Trans-Gender')
]

JOB_CITY_CHOICES = [
    ('Bengaluru', 'Bengaluru'),
    ('Chennai', 'Chennai'),
    ('Delhi', 'Delhi'),
    ('Hyderabad', 'Hyderabad'),
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune'), 
    ('Remote(WFH)', 'Remote(WFH)')
]

class CreateResumeForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget= forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices= JOB_CITY_CHOICES, widget= forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = [ 'user','name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']

        labels = {'name':'Full Name :', 'dob':'Date Of Birth :', 'gender': 'Gender :', 'locality': 'Locality :', 'city': 'City :', 'pin': 'PIN Code :', 'state': 'State :', 'mobile': 'Mobile No. :', 'email': 'Email ID :', 'job_city': 'Job Preffered Cities :', 'profile_image': 'Profile Photo :', 'my_file': 'Attachment :'}

        widgets = {
            
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id': 'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }


class UpdateResumeForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget= forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices= JOB_CITY_CHOICES, widget= forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = [ 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
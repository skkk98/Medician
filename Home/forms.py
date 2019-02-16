from django.contrib.auth.models import User
from .models import Detailuser
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    Type = forms.CharField(widget=forms.Select(choices=(('Doctor','DOCTOR'),('Patient','PATIENT'))))
    specialization = forms.CharField(widget=forms.Select(choices=(('Pathologist','PATHOLOGIST'), ('Radiologist', 'RADIOLOGIST'),('Obstetrician', 'OBSTETRICIAN'),('Cardiologist','CARDIOLOGIST'),('Endocrinologist','ENDOCRINOLOGIST'),('', '---------'))), required=False)
    class Meta:
        model = User, Detailuser
        fields = ['username', 'name', 'email', 'password', 'confirm_password', 'Type', 'specialization']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    Type = forms.CharField(widget=forms.Select(choices=(('Doctor','DOCTOR'),('Patient','PATIENT'))))
    specialization = forms.CharField(widget=forms.Select(choices=(('Pathologist','PATHOLOGIST'), ('Radiologist', 'RADIOLOGIST'),('Obstetrician', 'OBSTETRICIAN'),('Cardiologist','CARDIOLOGIST'),('Endocrinologist','ENDOCRINOLOGIST'),('', '---------'))), required=False)
    class Meta:
        model = User, Detailuser
        fields = ['username', 'password', 'Type', 'specialization']

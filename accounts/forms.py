from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(name=username)
        if qs.exists():
            raise forms.ValidationError('Username Already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email Already taken')
        return email

    def clean(self):
        data = self.cleaned_data
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password2')
        if pass1 != pass2:
            raise forms.ValidationError('Password Donot match')
        else:
            return data

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

class CompanyRegisterForm(forms.Form):
    compname = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    location = forms.CharField(widget=forms.TextInput)

    def clean_username(self):
        compname = self.cleaned_data.get("compname")
        qs = User.objects.filter(name=compname)
        if qs.exists():
            raise forms.ValidationError('Company name Already in use')
        return compname

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email Already taken')
        return email

    def clean(self):
        data = self.cleaned_data
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password2')
        if pass1 != pass2:
            raise forms.ValidationError('Password Donot match')
        else:
            return data

class CompanyLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

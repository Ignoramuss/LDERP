from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.RegexField(regex=r'^[\w\d]+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='Unique User Name eg: ShivB')),
                            label='', error_messages={'invalid': _("This value contains only letters, numbers and underscores.")})
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class SignUpForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': "Full Name eg: Shiv B"}))
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': ' Confirm Password'}))


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^[\w\d]+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='Unique User Name eg: ShivB')),
                            label='', error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})
    first_name = forms.RegexField(regex=r'^\w+$', label='', max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': "First Name eg: Shiv"}))
    last_name = forms.RegexField(regex=r'^\w+$', label='', max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': "Last Name eg: Bhosale"}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='Email')))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder='Password')), )
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder='Confirm Password')))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean_email(self):
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("This email is already taken. Please input another one."))

    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


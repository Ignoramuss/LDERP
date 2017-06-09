from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class SignUpForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': "Full Name eg: Shiv B"}))
    email = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': ' Confirm Password'}))
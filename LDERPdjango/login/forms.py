from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import StudentInfo, ParentalMetricScore


class LoginForm(AuthenticationForm):
    username = forms.RegexField(regex=r'^[\w\d]+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='Unique User Name eg: ShivB')),
                            label='', error_messages={'invalid': _("This value contains only letters, numbers and underscores.")})
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

# class SignUpForm(forms.Form):
#     name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': "Full Name eg: Shiv B"}))
#     email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#     password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
#     confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': ' Confirm Password'}))


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

# class StudentInfoForm(forms.Form):
#     stud_name = forms.RegexField(required=True, regex=r'^\w+$', label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': "First Name eg: Shiv", 'autofocus':'true'}))
#     stud_school = forms.RegexField(required=True, regex=r'^\w+$', label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': "Student's School's Name"}))
#     stud_standard = forms.RegexField(required=True, regex=r'^\w+$', label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': "Student's Standard"}))
#     stud_div = forms.RegexField(required=True, regex=r'^\w+$', label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': "Student's Division"}))
#
#     date_of_fill = forms.DateField(required=True, input_formats=['%d-%m-%Y'], label='',widget=forms.DateInput(attrs={'placeholder': "Date of Filling", 'type':"date"}))
#     date_of_birth = forms.DateField(required=True, input_formats=['%d-%m-%Y'], label='', widget=forms.DateInput(attrs={'placeholder': "Date of Birth", 'type':"date"}))
#
#     father_name = forms.CharField(required=True, label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': "Father's Full Name", 'autofocus':'true'}))
#     father_contact  = forms.CharField(required=True, label='', max_length=10, widget=forms.TextInput(attrs={'placeholder': "Eg 98xxxxxxx0"}))
#     father_email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs=dict(required=True, max_length=200, placeholder="Father's Email")))
#     father_education = forms.CharField(required=True, label='', max_length=200,widget=forms.TextInput(attrs={'placeholder': "Father's Education"}))
#     father_occupation = forms.CharField(required=True, label='', max_length=200,widget=forms.TextInput(attrs={'placeholder': "Father's Occupation"}))
#
#     mother_name = forms.CharField(required=True, label='', max_length=200,  widget=forms.TextInput(attrs={'placeholder': "Mother's Full Name",'autofocus': 'true'}))
#     mother_contact = forms.CharField(required=True, label='', max_length=10, widget=forms.TextInput(attrs={'placeholder': "Eg 98xxxxxxx0"}))
#     mother_email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs=dict(required=True, max_length=200, placeholder="Mother's Email")))
#     mother_education = forms.CharField(required=True, label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': "Mother's Education"}))
#     mother_occupation = forms.CharField(required=True, label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': "Mother's Occupation"}))
#
#     letter_identification = forms.BooleanField()
#     let_sound_assoc = forms.BooleanField()
#     spelling = forms.BooleanField()
#     reading = forms.BooleanField()
#     comprehension = forms.BooleanField()
#     composition = forms.BooleanField()
#     grammar = forms.BooleanField()
#
#     number_identification = forms.BooleanField()
#     forget_tables = forms.BooleanField()
#     carry_borr = forms.BooleanField()
#     frac_dec = forms.BooleanField()
#     problem_int = forms.BooleanField()
#     algebra = forms.BooleanField()
#
#     awareness = forms.IntegerField()
#     acceptance = forms.IntegerField()
#     active_participation = forms.IntegerField()
#     emo_support_provided = forms.IntegerField()
#     strength_awareness = forms.IntegerField()
#     parenting_style = forms.IntegerField()


class SearchForm(forms.Form):
    search = forms.RegexField(required=True, regex=r'^\w+$', label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': "Search for a Name", 'autofocus': 'true', "class":"form-control"}))
    disability = forms.ChoiceField(choices=[(1, "Show All"), (2,  "D1"), (3, "D2")], widget=forms.widgets.ChoiceWidget(attrs={"class":"filter-make filter form-control", "data-filter":"disability" }))
    age_group = forms.ChoiceField(choices=[(1, "Show All"), (2, "5-10"), (3, "10-15")], widget=forms.widgets.ChoiceWidget(attrs={"class": "filter-model filter form-control", "data-filter":"age_group"}))
    gender = forms.ChoiceField(choices=[(1, "Show All"), (2, "Male"), (3, "Female")], widget=forms.widgets.ChoiceWidget(attrs={"class": "filter-type filter form-control", "data-filter":"gender"}))
    education = forms.ChoiceField(choices=[(1, "Show All"), (2, "Grade 5"), (3, "Grade 10")], widget=forms.widgets.ChoiceWidget(attrs={"class": "filter-price filter form-control", "data-filter":"education"}))

class StudentInfoModelForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        exclude = ()
        widgets = {
            'stud_name':forms.TextInput(attrs={'placeholder': "First Name eg: Shiv", 'autofocus':'true'}),
            'stud_school':forms.TextInput(attrs={'placeholder': "Student's School's Name"}),
            'stud_standard':forms.TextInput(attrs={'placeholder': "Student's Standard"}),
            'stud_div':forms.TextInput(attrs={'placeholder': "Student's Division"}),

            'date_of_fill':forms.DateInput(attrs={'placeholder': "Date of Filling", 'type':"date"}),
            'date_of_birth':forms.DateInput(attrs={'placeholder': "Date of Birth", 'type':"date"}),

            'father_name':forms.TextInput(attrs={'placeholder': "Father's Full Name", 'autofocus': 'true'}),
            'father_contact':forms.TextInput(attrs={'placeholder': "Eg 98xxxxxxx0"}),
            'father_email':forms.TextInput(attrs=dict(required=True, max_length=200, placeholder="Father's Email")),
            'father_education':forms.TextInput(attrs={'placeholder': "Father's Education"}),
            'father_occupation':forms.TextInput(attrs={'placeholder': "Father's Occupation"}),

            'mother_name': forms.TextInput(attrs={'placeholder': "Mother's Full Name", 'autofocus': 'true'}),
            'mother_contact': forms.TextInput(attrs={'placeholder': "Eg 98xxxxxxx0"}),
            'mother_email': forms.TextInput(attrs=dict(required=True, max_length=200, placeholder="Mother's Email")),
            'mother_education': forms.TextInput(attrs={'placeholder': "Mother's Education"}),
            'mother_occupation': forms.TextInput(attrs={'placeholder': "Mother's Occupation"}),

            'language_disabilities': forms.CheckboxSelectMultiple(),
            'mathematical_disabilities': forms.CheckboxSelectMultiple(),
        }

class ParentalMetricScoreModelForm(forms.ModelForm):
    class Meta:
        model = ParentalMetricScore
        fields = ('metric_score', )
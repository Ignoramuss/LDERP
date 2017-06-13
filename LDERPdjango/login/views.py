from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import LoginForm, RegistrationForm, SearchForm, ParentalMetricScoreModelForm, StudentInfoModelForm
from .models import ParentalMetric, LanguageDisability, MathematicalDisability
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .multiforms import MultiFormsView
from django.contrib.admin.views.decorators import staff_member_required
import logging

# def login(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         login_form = LoginForm(request.POST)
#         signup_form = SignUpForm(request.POST)
#         # check whether it's valid:
#         if login_form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/loggedin/')
#             # check whether it's valid:
#         if signup_form.is_valid():
#             # process the data in form.cleaned_data as required
#             if signup_form.cleaned_data['password'] == signup_form.cleaned_data['confirm_password']:
#                 # coolz
#                 # redirect to a new URL:
#                 return HttpResponseRedirect('/registered/')
#             else:
#                 error_message = "Passwords don't match"
#                 return HttpResponseRedirect('/login/', args=(error_message, ))
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         login_form = LoginForm()
#         signup_form = SignUpForm()
#
#     return render(request, 'home.html', {'login_form': login_form, 'signup_form': signup_form})

class HomeView(MultiFormsView, LoginRequiredMixin):
    login_url = "login/"
    template_name = 'user_profile.html'
    form_classes = {'student': StudentInfoModelForm,
                    'search': SearchForm}
    success_url = '/'

    # def get_student_initial(self):
    #     return {'email': 'dave@dave.com'}
    #
    # def get_search_initial(self):
    #     return {'email': 'dave@dave.com'}

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context.update({"some_context_value": 'blah blah blah',
    #                     "some_other_context_value": 'blah'})
    #     return context

    def student_form_valid(self, form):
        student = form.save(commit=False)
        if self.request == "POST":
            if form.is_valid():
                pmforms = []
                for metric in ParentalMetric.objects.all():
                    pmform = ParentalMetricScoreModelForm(self.request.post, prefix=metric.metric_name)
                    if pmform.is_valid():
                        pmform.student = student
                        pmform.metric_type = metric
                        pmforms.append(pmform)
                    else:
                        return False
                for pmform in pmforms:
                    pmform.save()
                student.save()
            else:
                return False
        return True
        # return form.login(self.request, redirect_url=self.get_success_url())

    def search_form_valid(self, form):
        return True
        # user = form.save(self.request)
        # return form.signup(self.request, user, self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # Parental metric
        metric_dict = {}
        for metric in ParentalMetric.objects.all():
            pmform = ParentalMetricScoreModelForm(prefix=metric.metric_name)
            metric_dict.update({
                metric.metric_name: pmform
            })
        context.update({
            'metrics': metric_dict
        })
        return context



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            # message = 'Registered successfully'
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'home.html', {'form':LoginForm(),'signup_form':form})


# def register_success(request):
#     return render( request,  'home.html', {'message': 'Registered successfully'} )


# def logout_page(request):
#     logout(request)
#     return HttpResponseRedirect('/logout')

class LoginSignupView(auth_views.LoginView):
    def get_context_data(self, **kwargs):
        context = super(LoginSignupView, self).get_context_data(**kwargs)
        context.update({
            'signup_form': RegistrationForm(),
            'message':''
        })
        return context

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('login:change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     response = render(request, 'password_change.html', {
#         'form': form
#     })
#     response.set_cookie('password_changed', 'true')
#     return response

class CustomPasswordChangeView(auth_views.PasswordChangeView):
    def dispatch(self, request, *args, **kwargs):
        response = super(CustomPasswordChangeView, self).dispatch(request, *args, **kwargs)
        response.set_cookie('password_changed', 'true')
        return response

class CustomPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    def dispatch(self, request, *args, **kwargs):
        if 'password_changed' in request.COOKIES:
            response = super().dispatch(request, *args, **kwargs)
            response.delete_cookie('password_changed')
            return response
        else:
            return HttpResponseRedirect("/")

class CustomPasswordResetView(auth_views.PasswordResetView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.set_cookie('password_reset', 'true')
        return response

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    def dispatch(self, request, *args, **kwargs):
        if 'password_reset' in request.COOKIES:
            response = super().dispatch(request, *args, **kwargs)
            response.delete_cookie('password_reset')
            return response
        else:
            return HttpResponseRedirect("/")

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.set_cookie('password_reset_initiated', 'true')
        return response


class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    def dispatch(self, request, *args, **kwargs):
        if 'password_reset_initiated' in request.COOKIES:
            response = super().dispatch(request, *args, **kwargs)
            response.delete_cookie('password_reset_initiated')
            return response
        else:
            return HttpResponseRedirect("/")

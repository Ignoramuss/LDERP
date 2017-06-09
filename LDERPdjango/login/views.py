from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import LoginForm, SignUpForm, RegistrationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect

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

@login_required(login_url="login/")
def home(request):
    return render(request, "user_profile.html")


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
        if self.extra_context is not None:
            context.update(self.extra_context)
        return context


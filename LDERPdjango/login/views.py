from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm, SignUpForm

def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        login_form = LoginForm(request.POST)
        signup_form = SignUpForm(request.POST)
        # check whether it's valid:
        if login_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/loggedin/')
            # check whether it's valid:
        if signup_form.is_valid():
            # process the data in form.cleaned_data as required
            if signup_form.cleaned_data['password'] == signup_form.cleaned_data['confirm_password']:
                # coolz
                # redirect to a new URL:
                return HttpResponseRedirect('/registered/')
            else:
                error_message = "Passwords don't match"
                return HttpResponseRedirect('/login/', args=(error_message, ))

    # if a GET (or any other method) we'll create a blank form
    else:
        login_form = LoginForm()
        signup_form = SignUpForm()

    return render(request, 'home.html', {'login_form': login_form, 'signup_form': signup_form})

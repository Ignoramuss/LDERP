"""LDERPdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls import include
from .views import LoginSignupView
from . import views
from .forms import LoginForm

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # # url(r'^login/$', auth_views.login, {'template_name': 'home.html'}, name='login'),
    # url(r'^$', views.login, name='login'),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginSignupView.as_view(template_name='home.html', authentication_form=LoginForm), name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^register/success/$', views.register_success, name='register_success'),
    # url(r'^signup/$', views.signup, name='signup'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^dash/', TemplateView.as_view(template_name='user_profile.html'), name='dash'),
    # url(r'^admin/', admin.site.urls),
]

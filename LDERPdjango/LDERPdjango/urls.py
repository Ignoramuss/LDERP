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
from login.forms import LoginForm
from login.views import LoginSignupView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('login.urls')),
    # url(r'^', include('dashboard.urls')),
    url(r'^login/$', LoginSignupView.as_view(template_name='home.html', authentication_form=LoginForm), name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
]

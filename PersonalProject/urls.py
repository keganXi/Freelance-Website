"""PersonalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.project, name='project')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='project')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
import ContactApp.views as contact_views
import services.views as services_views


urlpatterns = [
    path('', include("home.urls")),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^Contact-Us/$', contact_views.Contact_us_view, name='contact-us-page'),
    re_path(r'^Services/$', services_views.Service_view, name='services-page'),
]


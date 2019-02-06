"""liftit_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
#from liftit_test.views import *
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^$', home.as_view())
    path('', views.home, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('register_owner', views.register_owner, name='register_owner'),
    path('register_vehicle', views.register_vehicle, name='register_vehicle'),
    path('check_license_plate', views.check_license_plate, name='check_license_plate'),
    path('check_owner', views.check_owner, name='check_owner'),
]

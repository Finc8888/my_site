from django.conf.urls import url, include
from django.contrib import admin
from contact.views import *

urlpatterns = [
    url(r'^bonuss/', bonus,name = 'index'),
]

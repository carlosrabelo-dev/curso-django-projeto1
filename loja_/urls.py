#from django.contrib import admin
from django.urls import path
from loja_.views import home



# HTTP REQUEST

urlpatterns = [
    path('', home), # /home/
    ]

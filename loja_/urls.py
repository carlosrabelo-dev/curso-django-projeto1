from django.contrib import admin
from django.urls import path
from loja_.views import home, sobre, contato



# HTTP REQUEST

urlpatterns = [
    path('', home), # /home/
    path('sobre/', sobre), #/sobre/
    path('contato/', contato), #/contato/
]

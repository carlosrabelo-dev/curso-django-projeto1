from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request, 'loja_/home.html')

def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('contato')

# Create your views here.

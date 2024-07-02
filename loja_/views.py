from django.shortcuts import render


def home(request):
    return render(request, 'loja_/home.html', context={
                  'name': 'Carlos Rabelo'
                  })


# Create your views here.

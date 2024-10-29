from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context: dict = {
        'title': 'Home',
        'content': 'Главная страница магащина - HOME'
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About page")
    
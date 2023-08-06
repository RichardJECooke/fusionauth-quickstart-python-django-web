from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app(request):
    return render(request, template_name='home.html')

def login(request):
    return render(request, template_name='account.html')

def change(request):
    return render(request, template_name='make-change.html')
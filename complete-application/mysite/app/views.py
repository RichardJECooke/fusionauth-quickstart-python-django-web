from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

def app(request):
    return render(request, template_name='home.html')

def account(request):
    if request.user.is_authenticated:
        return render(request, template_name='account.html')
    else:
        return redirect('oidc_authentication_init')

def change(request):
    if request.user.is_authenticated:
        return render(request, template_name='make-change.html')
    else:
        return redirect('oidc_authentication_init')
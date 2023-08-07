from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

def app(request):
    return render(request, template_name='home.html')

def account(request):
    if not request.user.is_authenticated:
        return redirect('oidc_authentication_init')
    return render(request, 'account.html')


def change(request):
    if not request.user.is_authenticated:
        return redirect('oidc_authentication_init')
    return render(request, 'make-change.html')
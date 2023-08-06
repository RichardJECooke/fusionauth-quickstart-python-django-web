from django.urls import path

from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('account/', views.account, name='account'),
    path('make-change/', views.change, name='change'),
]

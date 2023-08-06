from django.urls import path

from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('login/', views.login, name='login'),
    path('make-change/', views.change, name='change'),
]

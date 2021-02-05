from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('index/', views.indexView, name='home'),
    path('index/register', views.registerView, name='register'),
    path('index/login', views.loginView, name='login')
]

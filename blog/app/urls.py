from django.contrib import admin
from django.urls import path, include

from app.views import newView
from . import views

urlpatterns = [
    path('index/', views.newView, name='home'),
    path('index/login', views.loginView, name='login')
]

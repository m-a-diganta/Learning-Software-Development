from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('promt/', views.prompt, name='prompt'),
    path('temp-tag/', views.temp_tag, name='temp_tag'),
]
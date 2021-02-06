from django.contrib import admin
from django.urls import path, include
from . import views
# from .views import home

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
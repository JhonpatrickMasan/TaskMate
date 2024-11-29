from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing page route
]

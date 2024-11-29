# myapp/views.py
from django.shortcuts import render, redirect

# Create your views here.

def landing_page(request): #The landing page where the user goes through when entering the web
    return render(request, 'landing_page.html')

from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request,'register.html')
    
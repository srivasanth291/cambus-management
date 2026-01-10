from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'account/home.html')

def login(request):
    return render(request,'account/login.html')

def dashboard(request):
    return render(request,'account/dashboard.html')

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def home(request):
    return render(request,'account/home.html')

def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
             
    return render(request,'account/login.html')

def dashboard(request):
    return render(request,'account/dashboard.html')

# Create your views here.

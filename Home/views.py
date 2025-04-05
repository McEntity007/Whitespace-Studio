from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Home.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')    

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name= name, email= email, phone= phone, message= message, date = datetime.today())
        contact.save()
        messages.success(request, "Your form has successfully submitted.")
    return render(request, 'contact.html')

    
def interior(request):
    return render(request, 'interior.html')

def exterior(request):
    return render(request, 'exterior.html')

def customization(request):
    return render(request, 'customization.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')




# registration / login
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, "Your have registered successfully. Go to login page Now!")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/dashboard/")
        else:
            messages.warning(request, "Credentials are incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("/login")

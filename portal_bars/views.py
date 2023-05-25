from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Project
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.db import IntegrityError



def registration(request):

    if request.method == "POST":
        login = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=login).exists() :
            messages.error(request, "Уже существует")
            return render(request, 'portal/registration.html')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Уже существует")
            return render(request, 'portal/registration.html')
        else:
            user = User.objects.create_user(username=login, email=email, password=password)
            user.save()
            return redirect('home')

    return render(request, 'portal/registration.html',)

def home(request):
    return render(request, 'portal/home.html',)

def deliver(request):
    projects = Project.objects.all()
    return render(request, 'portal/deliver.html', {'projects':projects})

def restaurant(request):
    projects = Project.objects.all()
    return render(request, 'portal/restaurant.html', {'projects':projects})


def authorization(request):
    projects = Project.objects.all()
    return render(request, 'portal/authorization.html', {'projects':projects})

def index(request):
    projects = Project.objects.all()
    return render(request, 'portal/index.html', {'projects':projects})

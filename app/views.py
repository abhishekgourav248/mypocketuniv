from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .backends import EmailBackEnd
from django.core.files.storage import FileSystemStorage


def ShowLoginPage(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            return HttpResponseRedirect('app/AdminHome')
        elif request.user.is_faculty == True:
            return HttpResponseRedirect('app/StaffHome/')
        elif request.user.is_student == True:
            return HttpResponseRedirect('app/StudentHome/')
    else:
        return render(request, 'app/login.html')


def dologin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            "email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.is_superuser == True:
                return HttpResponseRedirect('app/AdminHome/')
            elif user.is_faculty == True:
                return HttpResponseRedirect('app/StaffHome/')
            elif user.is_student == True:
                return HttpResponseRedirect('app/StudentHome/')
        else:
            return HttpResponse('Invalid')


@login_required(login_url="login")
def dologout(request):
    logout(request)
    return redirect('/')


@login_required(login_url="login")
def index(request):
    if request.user.is_superuser == True and request.user.is_staff == True:
        return render(request, 'app/AdminHome.html')
    else:
        dologout(request)


@login_required(login_url="login")
def StaffHome(request):
    if request.user.is_faculty == True:
        return render(request, 'app/StaffHome.html')
    else:
        dologout(request)


@login_required(login_url="login")
def StudentHome(request):
    if request.user.is_student == True:
        return render(request, 'app/StudentHome.html')
    else:
        dologout(request)

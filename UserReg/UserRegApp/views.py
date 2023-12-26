from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .import views
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_registration(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confpassword = request.POST.get("conpassword")

        if password != confpassword:
            return HttpResponse("Your Password and Confirmed password not same.")
        else:
            user = User.objects.create_user(uname,email,password)
            user.save()
            return redirect(views.user_login)

    return render(request,"registration.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect(views.home)
        else:
            return HttpResponse("Username or Password is incorrect.")
    return render(request,"login.html")

@login_required(login_url="login")
def home(request):
    return render(request,"home.html")

def user_logout(request):
    logout(request)
    return redirect(views.user_login)
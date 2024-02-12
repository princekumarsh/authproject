from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
# Create your views here.

def index(request):
    # if request.user.is_anonymous:
    #     return HttpResponse("Hello, anonymous user!")
    # else:
    #     return HttpResponse(f"Hello, {request.user.username}!")
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request, "index.html")
    

def loginUser(request):
    if request.method=="POST":

        username=request.POST["username"]
        password=request.POST["password"]

        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/login")
        
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")
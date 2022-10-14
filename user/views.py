from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth import authenticate, login as loginsession
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "GET":
        return render(request,'signup.html')
    elif request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if not None:
            User.objects.create_user(username=username, password=password, phone=phone, address=address)
            return redirect('/user/login')


def login(request):
        if request.method == "GET":
            return render(request,'login.html')
        elif request.method =="POST":
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                loginsession(request, user)
                print("to home")
                return redirect('/user/home')

            else:
                return redirect('/user/login')


@login_required
def home(request):
    if request.method == "GET":
        return render(request,'home.html')
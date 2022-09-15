from django.shortcuts import render


def home(request):
    return render(request, 'auth/home.html')


def signup(request):
    return render(request, 'auth/signup.html')


def login(request):
    return render(request, 'auth/login.html')


def logout(request):
    pass

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'auth/home.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        mail = request.POST.get('mail')

        new_user = User.objects.create_user(username, mail, password=password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()

        messages.success(request, 'Your account has been successfully created.')

        return redirect('login')

    return render(request, 'auth/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'auth/home.html')
        else:
            messages.error(request, 'Bad credentials.')
            return redirect('home')

    return render(request, 'auth/login.html')


def logout(request):
    pass

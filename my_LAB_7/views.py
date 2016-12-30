from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from my_LAB_7.forms import *


def signin(request):
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('success/')
                return render(request, 'signin.html', {'form': form})
        else:
                form = RegistrationForm()
        return render(request, 'signin.html', {'form': form})


def signin_success(request):
        return render(request, 'signin_success.html')


def signup(request):
        errors = []
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                if not username:
                        errors.append('Введите логин!')
                elif not password:
                        errors.append('Введите пароль!')
                else:
                        user = authenticate(username=username, password=password)
                        if user:
                                auth.login(request, user)
                                return redirect('success/')
                        else:
                                errors.append('Неправильный логин или пароль!')
                return render(request, 'signup.html', {'errors': errors, 'username': username})
        return render(request, 'signup.html', {'errors': errors})


@login_required
def signup_success(request):
        return render(request, 'signup_success.html')


@login_required
def logout_view(request):
        return render(request, 'logout.html')
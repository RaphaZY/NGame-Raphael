from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate, logout
from .decorators import user_is_admin, user_is_client
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dash')
            else:
                form.add_error(None, 'Invalid username or password')   
    return redirect('index')

def register_view_dash(request):
    if request.method == 'POST':
        form = DashUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastrado com sucesso!')
            return redirect('index')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Cadastrado com sucesso!')
            login(request, user)
            return redirect('index')
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
@user_passes_test(user_is_admin)
def admin_page(request):
    return redirect('dash')

@login_required
@user_passes_test(user_is_client)
def client_page(request):
    return redirect('dash')
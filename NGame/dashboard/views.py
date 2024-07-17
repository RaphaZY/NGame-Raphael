from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from catalog.models import *
# Create your views here.


@login_required
def dash(request):
    if request.user.is_superuser:
        games = Game.objects.all()
        return render(request, 'dashb/dashboard.html', {'games': games})
    else:
        return redirect ('index')
    
@login_required
def dash_users(request):
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'dashb/dash_users.html', {'users': users})
    else:
        return redirect ('index')
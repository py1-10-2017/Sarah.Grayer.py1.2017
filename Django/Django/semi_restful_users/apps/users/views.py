# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request): #two different methods route here, so if/else statement is used
    if request.method == "POST":
        print request.POST
        User.objects.create(full_name = request.POST["full_name"], email = request.POST["email"])
        return redirect('/')
    else:
        context = {
            "users": User.objects.all()
        }
        return render(request, "users/index.html", context)

def display(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=1)
        user.full_name = request.POST["full_name"]
        user.email = request.POST["email"]
        user.save()
        return redirect('/users')
    else:
        context = {
            "user":User.objects.get(id=user_id)
        }
    return render(request, "users/display.html", context)

def create(request):
    return render(request, "users/add.html")

def edit(request, user_id):
    context = {
        "user":User.objects.get(id = user_id)
    }
    return render(request, "users/edit.html", context)

def update(request, user_id):
    user_to_update = User.objects.get(id=user_id)
    user_to_update.full_name = request.POST["full_name"]
    user_to_update.email = request.POST["email"]
    user_to_update.save()
    return redirect('/users')

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')

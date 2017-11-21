from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect, reverse, HttpResponseRedirect
from .models import *
from ..review.models import Book, Author, Review
from django.contrib import messages

def index(request):
    return render (request, "login/index.html")

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return HttpResponseRedirect(reverse("review:home"))

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return HttpResponseRedirect(reverse("review:home"))

def home(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render (request, "login/home.html", context)
    return HttpResponse ("HOME")

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    unique_ids= user.reviews_left.all().values("book").distinct()
    unique_books=[]
    for book in unique_ids:
        unique_books.append(Book.objects.get(id=book['book']))
    context={
        'user': user,
        'unique_book_reviews': unique_books
    }
    return render(request, "login/profile.html", context)
    return HttpResponse ("Profile info")

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render (request, "books/index.html")

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] =  result.id
    return redirect ('/home')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] =  result.id
    return redirect ('/home')

def home(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect ('/')
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render (request, "books/welcome.html", context)

def new(request):
    if 'user_id' in request.session:
        #context = {
            #"authors":Author.objects.all()
        #}
        return render (request, "books/add.html")
    #return HttpResponse ("NEW - details of new book and review")
    #else:
        #return redirect('/')

def create(request):
    errors = Review.objects.validate_review(request.POST)

    if errors:
        for err in errors:
            messages.error(request, err)
    #else:
        #Review.objects.create(
            #book = request.POST['title'],
            #reviewer = request.session['user_id'],
            #review = request.POST['review'],
            #rating = request.POST['rating'],
        #)
    book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id
    return redirect('/{}'.format(book_id))

def review(request, book_id):
    context = {
        "book":Book.objects.get(id=book_id)
    }
    return render(request, "books/review.html", context)
    #return HttpResponse ("BOOK REVIEW")

        #(
            #title = request.POST['title'],
            #reviewer = request.session['user_id'],
            #review = request.POST['review'],
            #rating = request.POST['rating'],
            #author = request.POST['author'],
        #)
    #return redirect('/review')
    #return HttpResponse ("CREATE BOOK REVIEW - add to reviews")

def profile(request):
    return HttpResponse ("PROFILE")


def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

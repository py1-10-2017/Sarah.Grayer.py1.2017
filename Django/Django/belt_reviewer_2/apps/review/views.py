from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from .models import Review, Author, Book
from ..login.models import User
from django.contrib import messages

def home(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'recent': Review.objects.recent_and_not()[0],
        'more': Review.objects.recent_and_not()[1]
    }
    return render(request, "review/home.html", context)

def add(request):
    context = {
        "authors": Author.objects.all()
    }
    return render (request, "review/add.html", context)
    return HttpResponse("add book")

def create(request):
    errs = Review.objects.validate_review(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id
    #return HttpResponse("Good?")
    return redirect('/books/{}'.format(book_id))

def display(request, book_id):#book_id defined in create route, review went through validations
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render (request, "review/display.html", context)
    return HttpResponse("Display review")

def create_addl(request, book_id):
    the_book = Book.objects.get(id=book_id)
    new_book_data={
        'title': the_book.title,
        'author': the_book.author.id,
        'rating': request.POST['rating'],
        'review': request.POST['review'],
        'new_author': ''
    }
    errs = Review.objects.validate_review(new_book_data)
    if errs:
        for e in errs:
            messages.error(reques, e)
    else:
        Review.objects.create_review(new_book_data, request.session['user_id'])
    return redirect('/books/'+book_id)
    return HttpResponse ("another review")

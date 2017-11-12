from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render (request, "words/index.html")

def process_form(request):
    new_word = {}
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key != "show-big":
            new_word[key] = value
        if key == "show-big":
            new_word['big'] = "big"
        else:
            new_word['big']= ""
    new_word['created_at']= datetime.now().strftime("%B %d, %Y, %H:%M %p")
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    temp_list = request.session['words']
    temp_list.append(new_word)
    request.session['words'] = temp_list
    for key, value in request.session.__dict__.iteritems():
        print key, value
    print "created at", new_word

    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect ('/')

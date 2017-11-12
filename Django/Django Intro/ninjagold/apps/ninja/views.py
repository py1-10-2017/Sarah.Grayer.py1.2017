from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render (request, "ninja/index.html")

def reset(request):
    request.session['gold'] = 0
    del request.session['logs']
    return redirect('/')

def process_money(request):
    new_gold = 0
    action = 'earned'
    building = request.POST['building']

    if building == 'farm':
        new_gold = random.randint(10,21)
    elif request.POST['building'] == 'cave':
        new_gold = random.randint(5,11)
    elif request.POST['building'] == 'house':
        new_gold = random.randint(2,6)
    else:
        new_gold = random.randint(-50,51)
        if new_gold < 0:
            action = 'lost'

    timestamp = datetime.now().strftime("%H:%M on %m/%d/%Y")
    this_log = {
        "class": action,
        "message": "You {} {} golds from the {} ({})".format (action, new_gold, building, timestamp)
    }

    try:
        log_list = request.session['logs']
    except KeyError:
        log_list = []

    request.session['gold'] += new_gold
    log_list.append(this_log)
    request.session['logs'] = log_list

    print this_log
    print log_list

    return redirect('/')

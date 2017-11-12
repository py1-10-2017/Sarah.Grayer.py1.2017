from __future__ import unicode_literals
from products import items #pre-populated items list in products.py
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if "last_trans" in request.session.keys():
        del request.session['last_trans'] #clear out last_trans fom session, prevent multiple charges w/each view
    context = {
        "items":items
    }
    return render (request, "shop/index.html", context)

def buy(request, item_id): #find item from items list w/url's item_id, matching 'id' key on item
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])
    #handle exceptions for session keys if they do not exist yet
    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0

    request.session['total_charged'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_trans'] = amount_charged
    return redirect('/checkout')

def checkout(request):
    return render (request, 'shop/checkout.html')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def surveys(request):
    return HttpResponse("Placeholder - display all the surveys created")

def new_survey(request):
    return HttpResponse("Placeholder for users to add a new survey")

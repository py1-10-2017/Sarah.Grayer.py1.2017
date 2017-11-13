# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#create models below
class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    books = models.ManyToManyField(Book, related_name="authors") #ManyToManyField establishes the MTM relationship between the tables, how Django handles the MTM w/o needing a 3rd linking table. Can add this Field to either class, doesn't matter which.
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.EmailField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    notes = models.TextField(default= ' ')

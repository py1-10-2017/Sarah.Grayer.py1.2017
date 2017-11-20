# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        if len(self.filter(email = post_data['email']))>0:
            user = self.filter(email = post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(),user.password.encode()):
                errors.append('Password is incorrect')
        else:
            errors.append('Email and/or password are incorrect')
        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []
        if len(post_data['name'])<3:
            errors.append("Please enter a name of at least 3 characters.")
        if len(post_data['alias'])<3:
            errors.append("Please enter an alias of at least 3 characters.")
        if not re.match(NAME_REGEX, post_data['name']) or not re.match(NAME_REGEX, post_data['alias']):
            errors.append("Please enter a name and alias with only letters.")
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("Invalid email")
        if len(User.objects.filter(email = post_data['email']))>0:
            errors.append("Email already in use")
        if len(post_data['password'])<8:
            errors.append("Please enter a Password with at least 8 characters.")
        if post_data['confirm_password'] != post_data['password']:
            errors.append("Passwords do not match.")
        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))
            new_user = self.create(
                name = post_data['name'],
                alias = post_data['alias'],
                email = post_data['email'],
                password = hashed
            )
            return new_user
        return errors

class ReviewManager(models.Manager):
    def validate_review(self, post_data):
        errors = []
        if len(post_data['title'])<1 or len(post_data['review'])<1:
            errors.append("Please enter Book Title and Review.")
        if not "author" in post_data or len(post_data['new_author'])<3:
            errors.append("New author names must be at least 3 characters.")
        if "author" in post_data and len(post_data['new_author'])>0:
            errors.append("Please either select an author or enter a new author.")
        if not int(post_data['rating'])>0 or not int(post_data['rating'])<=5:
            errors.append("Invalid rating")
        return errors

    def create_review(self, clean_data, user_id):
        the_author = None
        if len(clean_data['new_author'])<1:
            the_author = Author.objects.get(id=int(clean_data['author']))
        else:
            the_author = Author.objects.create(name=clean_data['new_author'])

        the_book = None
        if not Book.objects.filter(title=post_data['title']):
            the_book = Book.objects.create(
                title=clean_data['title'], author = the_author
            )
        else:
            the_book = Book.objects.get(title=clean_data['title'])
        return self.create(
            review = clean_data['review'],
            rating = clean_data['rating'],
            book = the_book,
            reviewer = User.objects.get(id=user_id),
        )

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    #reviews = models.ManyToManyField(Review, related_name = "Users")
    def __str__(self):
        return self.email

class Author(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Author, related_name = "books")
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name = "reviews")
    reviewer = models.ForeignKey(User, related_name = "reviews_left")
    created_at = models.DateTimeField(auto_now_add = True)
    review = models.TextField()
    rating = models.IntegerField()
    objects = ReviewManager()
    def __str__(self):
        return "Book:{}".format(self.book)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re #REGEX
import bcrypt #
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        # check db for post_data email
        if len(self.filter(email = post_data['email'])) > 0:#email in db
            #check pw
            user = self.filter(email = post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('Password is incorrect')
        else:
            errors.append('Email and/or password incorrect')
        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []
        #names
        if len(post_data['name'])<3 or len(post_data['alias'])<3:
            errors.append("Please enter Name's with at least 3 characters.")
        if not re.match(NAME_REGEX, post_data['name']) or not re.match(NAME_REGEX, post_data['alias']):
            errors.append("Please enter Name's with only letters")

        #email
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("Invalid email")
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("Email already in use")

        #pw
        if len(post_data['password'])<8:
            errors.append("Please enter a Password with at least 8 characters.")
        if post_data['confirm_pw'] != post_data['password']:
            errors.append("Passwords do not match.")

        if not errors:
            #make User and hash pw
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                name = post_data['name'],
                alias = post_data ['alias'],
                email = post_data ['email'],
                password = hashed
            )
            return new_user
        return errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    def __str__(self):
        return self.email

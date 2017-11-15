# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)

class UserManageer(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['full_name']) < 5:
            errors ['full_name'] = "Name should be more than 5 characters"
        if len(postData['email']) < 5:
            errors ['full_name'] = "Email should be more than 5 characters"
        return errors

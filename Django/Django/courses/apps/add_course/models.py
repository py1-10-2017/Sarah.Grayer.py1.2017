# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, post_data):
        errors=[]
        if len(post_data['name'])<5:
            errors.append("Please enter name with more than five characters")
        if len(post_data['desc'])<15:
            errors.append("Please enter a description with more than fifteen characters")
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    desc = models.TextField()
    objects = CourseManager()

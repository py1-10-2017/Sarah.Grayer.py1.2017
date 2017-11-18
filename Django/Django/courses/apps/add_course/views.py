from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from .models import Course

def index(request):
    if request.method == "POST":
        Course.objects.create(name = request.POST["name"], desc = request.POST["desc"])
        return redirect ('/')
    else:
        context = {
            "courses":Course.objects.all()
        }
        return render(request, "add_course/index.html", context)

def create(request):
    errors = Course.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:
        Course.objects.create(
            name = request.POST['name'],
            desc = request.POST['desc']
        )
    return redirect('/')

def remove(request, course_id):
    context = {
        "course":Course.objects.get(id = course_id)
    }
    return render(request, "add_course/delete.html", context)

def delete(request, course_id):
    Course.objects.get(id = course_id).delete()
    return redirect ('/')

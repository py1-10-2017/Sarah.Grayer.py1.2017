from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course/create$', views.create),
    url(r'^add_course/(?P<course_id>\d+)/remove$', views.remove),
    url(r'^add_course/(?P<course_id>\d+)/delete$', views.delete),
]

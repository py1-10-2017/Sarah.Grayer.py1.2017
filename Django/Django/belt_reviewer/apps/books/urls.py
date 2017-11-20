from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^profile$', views.profile),
    url(r'^logout$', views.logout),
    url(r'^(?P<book_id>\d+)$', views.review),
]

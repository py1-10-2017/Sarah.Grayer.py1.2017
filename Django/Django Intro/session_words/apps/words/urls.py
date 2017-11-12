from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^words/process$', views.process_form),
    url(r'^words/clear$', views.clear),
]

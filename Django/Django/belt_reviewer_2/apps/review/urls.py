#review urls
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^add$', views.add, name = 'add'),
    url(r'^create', views.create, name = 'create'),
    url(r'^(?P<book_id>\d+)$', views.display),
    url(r'^(?P<book_id>\d+)/create$', views.create_addl),
]

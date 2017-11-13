from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register), # display 'placeholder for users to create a new user record'
    url(r'^login$', views.login), #display 'placeholder for users to login'
    url(r'^users/new$', views.register), #have the same method that handles /register also handle the url request of /users/new
    url(r'^users$', views.users), #display 'placeholder to later display all the list of users'
]

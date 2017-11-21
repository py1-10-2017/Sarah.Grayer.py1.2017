from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login, name = 'login'),
    url(r'^home$', views.home),
    #url(r'^show_profile$', views.show_profile),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^user/(?P<user_id>\d+)$', views.profile)
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #blank, index page
    url(r'^new$', views.new), #begins & ends w/new, views page & "new" method
    url(r'^create$', views.create), #begins & ends w/create, views page & "create" method
    url(r'^(?P<blog_id>\d+)$', views.show), #begins & ends w/a # which is a blog id, passes into "show" method
    url(r'^(?P<blog_id>\d+)/edit$', views.edit), # of blog id / edit, # passed to "edit"
    url(r'^(?P<blog_id>\d+)/delete$', views.destroy) # of blog id / delete
]

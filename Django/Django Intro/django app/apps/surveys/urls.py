from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.surveys), #display placeholder to display all the surveys created. URL shows 8000/surveys/
    url(r'^new$', views.new_survey), #display placeholder for users to add a new survey. URL shows 8000/surveys/new
]

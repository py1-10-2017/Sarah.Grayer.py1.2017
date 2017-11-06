from django.conf.urls import url # gives access to the function url
from . import views # explicitly imports views.py in current folder
url patterns = [
    url(r'^', views.index) # uses the url method (we have called url, passing in a regex to find a match for an incoming http request), similar to @app.route in flask. The r after the ( tells python to interpret the following as a string, so it won't escape any special characters, useful w/regex strings. In this case, r'^$' is looking for an empty string in the url, and since pattern matches, will run the views.index method. Passing in views.index gives access to the functions in our views file.
]

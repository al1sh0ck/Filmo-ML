from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import get_films, indexview, signin_view, register_view

urlpatterns = [
path("", indexview, name="index"),
path("api/films/", get_films, name="get_films"),
path("signin/", signin_view, name="signin"),
path("create_account/", register_view, name="create_account"),
] + staticfiles_urlpatterns()
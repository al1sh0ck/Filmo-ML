from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import indexview, signin_view, register_view

urlpatterns = [
path("", indexview, name="index"),
path("signin/", signin_view, name="signin"),
path("create_account/", register_view, name="create_account"),
path('logout/', views.logout_view, name='logout'),
] + staticfiles_urlpatterns()
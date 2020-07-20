from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.logins),
    path('register', views.register),
    path('logout', views.logout_view)
]
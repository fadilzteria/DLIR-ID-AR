from django.urls import path

from . import views

app_name = 'kitab'
urlpatterns = [
    path('', views.upload)
]
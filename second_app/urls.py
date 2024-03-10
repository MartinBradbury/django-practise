from django.urls import path
from . import views

urlpatterns = [
    path('secondview', views.secondview)
]
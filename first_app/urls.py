from django.urls import path
from . import views

urlpatterns = [
    path('firstview', views.firstview)
]
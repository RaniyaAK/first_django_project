
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('all_members/',views.all_members),
    path('all_members/details/<int:id>', views.details),
]


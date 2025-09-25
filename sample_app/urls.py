
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('',views.index),
    path('',views.all_members,name='all_members'),
    path('all_members/details/<int:id>', views.details,name="details"),
    path('testing/', views.testing, name='testing'),
    path('details/<int:id>',views.details,name='update_member'),
    path('add/', views.add,name='add'), 
    path('add/add_member/',views.add_member,name='add_member'),
    path('delete_member/<int:id>',views.delete_member,name='delete_member'),   
    path('update_member/<int:id>',views.update_member,name='update_member'),


]


from django.contrib import admin
from django.urls import path
from .views import apiView, employee_list, employee_detail, post_employee

urlpatterns = [
  
  path('',apiView, name = 'apiView'),
  path('list/',employee_list, name = 'employee_list'),
   path('details/<int:pk>/',employee_detail, name = 'employee_detail'),
    path('post/',post_employee, name = 'post_employee'),
    
]

from django.contrib import admin
from django.urls import path
from .views import employee_list,employee_detail
urlpatterns = [
    path('list/',employee_list, name = 'list_employees'),
    path('detail/<int:pk>/',employee_detail, name = 'detail'),
    
]

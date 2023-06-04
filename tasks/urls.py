from .models import *
from .views import *
from django.urls import path

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('read/<int:task_id>/', read_task, name='read_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]

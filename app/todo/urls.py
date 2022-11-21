from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/list/', views.TaskListView.as_view(), name='task_list'),


]

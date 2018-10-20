from django.urls import path

from .views import TaskDetail, TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]

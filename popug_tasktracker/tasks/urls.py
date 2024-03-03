from django.urls import path
from . import views

urlpatterns = [
    path('assignee', views.AssigneeView.as_view(), name='assignee'),

    path('tasks', views.TaskView.as_view(), name='tasks')
]

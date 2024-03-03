from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer
from .models import Task, CustomUser
from random import choice


class TaskView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class AssigneeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        tasks = Task.objects.filter(task_status='In progress')
        for task in tasks:
            executor = choice(users)
            task.executor = executor
            task.save()

        return Response(status=status.HTTP_200_OK)

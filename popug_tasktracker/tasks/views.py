from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#from .producer import publish
from .serializers import TaskSerializer
from .models import Task, CustomUser
from random import choice


class TaskView(APIView):
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #publish("task.created", serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

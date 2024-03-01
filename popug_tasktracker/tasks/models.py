from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)


class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    task_status = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now_add=True)
    assignee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

from django.db import models

STATUS_CHOICE = {
    'In progress': 'In progress',
    'Completed': 'Completed'
}


class CustomUser(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)


class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    task_status = models.CharField(max_length=50, choices=STATUS_CHOICE)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now_add=True)
    executor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

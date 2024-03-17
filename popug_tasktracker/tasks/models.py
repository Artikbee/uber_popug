from django.db import models


class TaskStatus(models.TextChoices):
    NEW = 'new', 'New'
    DONE = 'done', 'Done'


class CustomUser(models.Model):
    public_id = models.IntegerField()
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    email = models.EmailField()


class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=TaskStatus.choices, default=TaskStatus.NEW)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now_add=True)
    executor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def is_completed(self):
        return self.status == TaskStatus.DONE

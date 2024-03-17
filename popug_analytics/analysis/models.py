from django.db import models


class CustomUser(models.Model):
    public_id = models.UUIDField()
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    email = models.EmailField()


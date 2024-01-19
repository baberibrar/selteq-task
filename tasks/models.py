from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=10, null=True, blank=True)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.task_name

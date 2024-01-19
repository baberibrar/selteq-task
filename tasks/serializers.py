from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(max_length=10, required=True)
    # scheduled_time is currently read-only

    class Meta:
        model = Task
        fields = ['id', 'task_name', 'scheduled_time']
        read_only_fields = ['id', 'scheduled_time']


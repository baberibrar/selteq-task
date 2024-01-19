from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task
from rest_framework.decorators import permission_classes
from .celery_tasks import add_task_to_db
import datetime


@permission_classes([IsAuthenticated])
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task_name = serializer.validated_data['task_name']
            scheduled_time_str = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            user_id = request.user.id
            add_task_to_db.apply_async(args=(user_id, task_name, scheduled_time_str), countdown=2)
            return Response({'status': 'success', 'message': 'Task added successfully'})
        else:
            return Response({'status': 'error', 'message': 'Invalid data'})

    def list(self, request, *args, **kwargs):
        queryset = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(queryset, many=True)
        return Response({'status': 'success', 'data': serializer.data})

# tasks/tasks.py
from celery import shared_task
from datetime import datetime
from .models import Task


@shared_task
def print_task_name(task_name):
    print(f"Task Name: {task_name}, Time: {datetime.now()}")


@shared_task
def add_task_to_db(user_id, task_name, scheduled_time_str):
    global scheduled_time
    try:
        if isinstance(scheduled_time_str, str):
            scheduled_time = datetime.strptime(scheduled_time_str, "%Y-%m-%dT%H:%M:%S")
        elif isinstance(scheduled_time_str, datetime):
            scheduled_time = scheduled_time_str

        # Move the task creation outside the elif block
        task = Task.objects.create(user_id=user_id, task_name=task_name, scheduled_time=scheduled_time)
        print(f"Task '{task_name}' scheduled for {scheduled_time}")
    except Exception as e:
        print(f"Error in add_task_to_db: {e}")

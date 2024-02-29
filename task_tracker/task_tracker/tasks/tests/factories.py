from factory import django

from task_tracker.tasks.models import Task

class TaskFactory(django.DjangoModelFactory):
    class Meta:
        model = Task
    
    name = "Task test"
    description = "Text description"
    estimate = 3.0
    state = "planned"
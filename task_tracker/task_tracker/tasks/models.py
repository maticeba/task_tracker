from django.db import models

# Create your models here.

class Task(models.Model):
    TASK_STATES = {
        "planned": "planned",
        "progress": "progress",
        "completed": "completed"
        }
    

    name = models.CharField(max_length=30)
    description = models.TextField()
    estimate = models.FloatField()
    state = models.CharField(choices=TASK_STATES, max_length=9)
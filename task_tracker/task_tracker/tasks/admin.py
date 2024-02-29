from django.contrib import admin
from task_tracker.tasks.models import Task
# Register your models here.
admin.site.register([Task])
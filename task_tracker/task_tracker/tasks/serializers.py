from django.forms import ValidationError
from rest_framework.serializers import ModelSerializer
from task_tracker.tasks.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def validate_state(self, attrs):
        if attrs != 'planned':
            raise ValidationError('Task can only be created in Planned state') #I am assuming you cant create task in progress or completed
        
        return attrs


class TaskPartialUpdateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['state']
    
    def validate(self, attrs):
        state = attrs.get('state')
        if state not in Task.TASK_STATES:
            raise ValidationError('Invalid task state')
        
        return attrs
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from task_tracker.tasks.models import Task
from task_tracker.tasks.serializers import TaskSerializer, TaskPartialUpdateSerializer

class TaskViewset(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        state = request.query_params.get('state')

        if state and state in Task.TASK_STATES:
            tasks = tasks.filter(state=state)
        elif state:
            return Response('Invalid state', status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # The challenge didn't mentioned anything about updating other fields of the task so i dissabled thi option 
        return Response('Method [PUT] not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskPartialUpdateSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        updated_task = self.get_object()
        updated_serializer = TaskSerializer(updated_task)
        
        return Response(updated_serializer.data)
    
    @action(detail=False, methods=['GET'])
    def status(self, request):
        tasks = self.queryset
        response = {
            "planned": 0,
            "progress": 0,
            "completed": 0
        }
        for task in tasks:
            response[task.state] += task.estimate

        return Response(response)    
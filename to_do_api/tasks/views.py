from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.routers import DefaultRouter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



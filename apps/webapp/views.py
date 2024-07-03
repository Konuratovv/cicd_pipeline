from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Task
from .serializers import TaskSerialzier, CreateTaskSerializer

# Create your views here.


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialzier


class CreateTaskAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer
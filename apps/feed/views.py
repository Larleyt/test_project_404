from django.shortcuts import render

from rest_framework import generics
from rest_framework import status, authentication, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TaskSerializer
from .models import Task


def homepage(request):
    return render(request, 'index.html')


class AllTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET'])
def get_task(request, task_id):
    task = Task.objects.get(id=task_id)
    serializer = TaskSerializer(task)
    return Response(serializer.data)
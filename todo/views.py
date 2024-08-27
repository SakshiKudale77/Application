from django.shortcuts import render
from rest_framework import generics
from .models import TodoTask
from .serializers import TodoTaskSerializer
# Create your views here.


class TodoTaskListCreateView(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer

class TodoTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer

class SearchByIDView(generics.RetrieveAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer
    lookup_field = 'id'
        
    def get_queryset(self):
        id = self.kwargs.get('id')
        return TodoTask.objects.filter(id=id)

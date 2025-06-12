from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.
class ListToDo(generics.ListAPIView):
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer
    
class DetailTodo(generics.RetrieveUpdateAPIView):
      queryset=ToDo.objects.all()
      serializer_class=ToDoSerializer
      
class CreateTodo(generics.CreateAPIView):
      queryset=ToDo.objects.all()
      serializer_class=ToDoSerializer
      
class DeleteTodo(generics.DestroyAPIView):
      queryset=ToDo.objects.all()
      serializer_class=ToDoSerializer


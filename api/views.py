from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serialisers import TaskSerialiser, PostSerialiser, UserSerializer
from .models import Task, Post

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiser
    permission_classes = (AllowAny,)

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiser
    permission_classes = (AllowAny,)

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser
    permission_classes = (AllowAny,)

class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser
    permission_classes = (AllowAny,)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser
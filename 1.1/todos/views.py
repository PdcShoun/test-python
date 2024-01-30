from django.http import Http404
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TodoListViews(APIView):
    def get(self, request):
        todos = TodoSerializer(Todo.objects.all(), many=True)
        return Response(todos.data)

    def post(self, request):
        todo = TodoSerializer(data=request.data)
        if todo.is_valid():
            todo.save()
            return Response(todo.data, status=status.HTTP_201_CREATED)
        return Response(todo.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailViews(APIView):
    def get_object(self, id):
        try:
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, id):
        todo = TodoSerializer(self.get_object(id))
        return Response(todo.data)

    def put(self, request, id):
        todo = TodoSerializer(self.get_object(id), data=request.data)
        if todo.is_valid():
            todo.save()
            return Response(todo.data)
        return Response(todo.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        todo = self.get_object(id)
        todo.delete()
        return Response({'delete': id}, status=status.HTTP_204_NO_CONTENT)

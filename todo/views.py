from django.contrib.auth import get_user_model
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer , UserSerializer

User = get_user_model()


@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        todo_serializers = TodoSerializer(todos, many=True)
        return Response(todo_serializers.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    else:
        return Response(None, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_view(request: Request, todo_id: int):
    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)

        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


# class base view

class TodosListApiView(APIView):
    def get(self, request: Request):
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, HTTP_200_OK)

    def post(self, request: Request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(None, status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    def get_object(self, todo_id: int):
        try:
            todos = Todo.objects.order_by('priority').all()
            return todos
        except Todo.DoesNotExist:
            return Response(None, HTTP_404_NOT_FOUND)

    def get(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer, status.HTTP_200_OK)

    def put(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(None, HTTP_404_NOT_FOUND)

    def delete(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


class TodosListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class TodosUpdateMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                              generics.GenericAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)


class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer


class TodoGenericUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer


class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    # user_id = User.objects.values('id')
    # print(user_id[0].values())


class UserGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

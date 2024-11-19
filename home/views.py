from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from todo.models import Todo


# Create your views here.
def index(request: HttpRequest):
    context = {
        'todos': Todo.objects.order_by('priority').all()
    }
    return render(request, 'home/index.html', context)


@api_view(['GET'])
def todos_json(request: Request):
    todos = list(Todo.objects.order_by('priority').all().values('title', 'is_done'))
    return Response({'todos': todos}, status.HTTP_200_OK)

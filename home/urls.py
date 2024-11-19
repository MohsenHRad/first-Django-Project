from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('json/', views.todos_json, name='todos_json')
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import TodosListApiView

router = DefaultRouter()
router.register('', views.TodosViewSetApiView)
urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('cbv/', TodosListApiView.as_view()),
    path('cbv/<int:todo_id>', views.todo_detail_view),
    path('mixins/', views.TodosListMixinApiView.as_view()),
    path('mixins/<pk>', views.TodosUpdateMixinApiView.as_view()),
    path('generics/', views.TodosGenericApiView.as_view()),
    path('generics/<pk>', views.TodoGenericUpdateApiView.as_view()),
    path('viewsets/', include(router.urls)),
    path('users/', views.UserGenericApiView.as_view())

]

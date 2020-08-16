from django.urls import path
from . import views

urlpatterns = [
    path('api/user/', views.UserListCreate.as_view()),
    path('api/list/', views.ListListCreate.as_view()),
    path('api/task/', views.TaskListCreate.as_view())
]

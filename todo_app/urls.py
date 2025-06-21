from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="todo-list"),
    path("remove/<int:pk>/", views.TodoDeleteView.as_view(), name="todo-delete"),
    path("add/",views.TodoCreateView.as_view(), name="todo-create"),
    path("update/<int:pk>/", views.TodoUpdateView.as_view(), name="todo-update"),
]

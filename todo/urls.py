from django.urls import path
from .views import TodoTaskListCreateView, TodoTaskRetrieveUpdateDestroyView, SearchByIDView

urlpatterns = [
    path('tasks/', TodoTaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TodoTaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('searchByID/<int:id>/', SearchByIDView.as_view(), name='search-by-id'),
]
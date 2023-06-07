from django.urls import path
from .views import list_tasks, create_task,delete_task,update_task,edit_task

urlpatterns = [
    path('',list_tasks),
    path('new/',create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'), # le pasa el ID para que sepa que tarea esta borrando.
    path('tasks/<int:task_id>/update/',update_task, name='update_task'),
    path('tasks/<int:task_id>/edit/', edit_task, name='edit_task'),

]
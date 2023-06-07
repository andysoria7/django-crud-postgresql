from django.shortcuts import render,redirect, get_object_or_404
from .models import Task

# Create your views here.

# Funcion para obtener las listas de tareas.
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request,'list_tasks.html',{
        'tasks': tasks
    })
    
# Funcion para crear las tareas y guardarlas.
def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save() # Guarda datos en la base de datos.
    return redirect('/tasks/')

# Funcion para borrar cada tarea.
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id) # Busca el objeto de la base de datos.
    task.delete() # Borra el dato de la base de datos.
    return redirect("/tasks/")

# Funcion que me trae los datos de la tarea en el formulario Edit Task.
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'edit_task.html', {'task': task})

# Funcion para actualizar cada tarea.
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('/tasks/')
    
    return redirect('/tasks/')  # Redirige a la lista de tareas después de actualizar
    



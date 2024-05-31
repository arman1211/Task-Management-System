from django.shortcuts import render,redirect
from task.forms import TaskForm
from task.models import TaskModel

# Create your views here.

def showTask(request):
    tasks = TaskModel.objects.all()
    return render(request, 'showtask.html',{'tasks': tasks})

def addTask(request):
    if request.method =='POST':
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            taskform.save()
            return redirect('showtask')
    else:
        taskform = TaskForm()
    return render(request, 'addtask.html',{'form': taskform})

def editTask(request,id):
    task = TaskModel.objects.get(pk=id)
    taskform = TaskForm(instance=task)
    if request.method =='POST':
        taskform = TaskForm(request.POST,instance=task)
        if taskform.is_valid():
            task.is_completed = True
            taskform.save()
            return redirect('showtask')
    
    return render(request, 'addtask.html',{'form': taskform})

def deleteTask(request,id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('showtask')
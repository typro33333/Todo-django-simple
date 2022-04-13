from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Count
from .models import TaskItem, TodoList
# Create your views here.
def TodoView(request):
  task_count = TodoList.objects.annotate(number_of_tasks=Count('taskitems'))
  task_item = TaskItem.objects.all()
  return render(request, 'base.html', {
    'todolist': task_count,
    'tasktodo': task_item,
  })

def addtodolist(request):
  x = request.POST['title']
  new_item = TodoList(title=x)
  new_item.save()
  return HttpResponseRedirect('/todoapp/')

def addtask(request):
  x = request.POST['name_task']
  y = request.POST['description']
  todo_list = TodoList.objects.get(title=request.POST['todo_list'])
  new_item = TaskItem(name_task = x, description = y, todo_list = todo_list)
  new_item.save()
  return HttpResponseRedirect('/todoapp/')

def donetask(request, i):
  x = TaskItem.objects.get(id = i)
  x.delete()
  return HttpResponseRedirect('/todoapp/')
from django.contrib import admin
from .models import TodoList, TaskItem

# Register your models here.
admin.site.register(TodoList)
admin.site.register(TaskItem)
from pyexpat import model
from django.db import models

TIME_SELECT = (
  ('S', 'Second'),
  ('M', 'Minutes'),
  ('H', 'Hours'),
)

# Create your models here.
class TodoList(models.Model):
  #id_todolist: models.AutoField(primary_key=True)
  title = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
  def __str__(self):
    return self.title

class TaskItem(models.Model):
  #id_task = models.AutoField(primary_key=True)
  name_task = models.CharField(max_length=100)
  description = models.TextField(max_length=200, null=True, blank=True)
  todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='taskitems')

  def __str__(self):
    return self.name_task
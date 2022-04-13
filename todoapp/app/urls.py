from django.urls import path
from .views import addtodolist, addtask, donetask, TodoView

urlpatterns = [
  ##################
  ###### API #######
  path('', TodoView),
  path('addtodolist/', addtodolist),
  path('addtask/', addtask),
  path('donetask/<int:i>/', donetask),
]
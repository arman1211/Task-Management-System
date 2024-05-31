from django.urls import path,include
from task.views import showTask,addTask,editTask,deleteTask

urlpatterns = [
    
    path("", showTask, name='showtask'),
    path('add/', addTask,name='addtask'),
    path('edit/<int:id>', editTask,name='edittask'),
    path('delete/<int:id>', deleteTask,name='deletetask')
]

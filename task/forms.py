from task.models import TaskModel
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
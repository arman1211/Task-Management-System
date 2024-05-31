from django.db import models
from category.models import CategoryModel
import datetime

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField(default=datetime.datetime.now())
    category = models.ManyToManyField(CategoryModel)

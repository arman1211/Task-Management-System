from django.urls import path,include
from category.views import addCategory

urlpatterns = [
    
    path("", addCategory, name='addcategory'),
    
]

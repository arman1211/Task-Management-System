from django.shortcuts import render
from .forms import CategoryForm

# Create your views here.

def addCategory(request):
    if request.method == 'POST':
        catagoryForm = CategoryForm(request.POST)
        if catagoryForm.is_valid():
            catagoryForm.save()
    catagoryForm = CategoryForm()
    return render(request, 'category.html',{'form': catagoryForm})

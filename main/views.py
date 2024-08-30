from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Item

# Create your views here.

def home_view(request):
    return render(request,'main/home.html')

def create_view(request):
    return render(request,'main/create.html')

def delete_view(request):
    return render(request,'main/delete.html')

def contact_view(request):
    return render(request,'main/contact.html')

def create_view(request):
    return render(request,'main/create.html')

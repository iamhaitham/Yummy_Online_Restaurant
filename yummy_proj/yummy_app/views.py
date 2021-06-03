from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.

def root(request):
    return  HttpResponse("This is a placeholder for root")

def category(request,category):
    context={
        "categoryName":category,
        "All_Dishes":models.getCategoryByName(category),
        "Number":3,
    }
    return render(request,"categories.html",context)
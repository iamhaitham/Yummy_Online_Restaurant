from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    return render(request, "home.html")


def category(request,category):
    context={
        "categoryName":category,
        "All_Dishes":models.getCategoryByName(category),
        "Number":3,
    }
    return render(request,"categories.html",context)

def cart(request):
    return render(request, "cart.html")
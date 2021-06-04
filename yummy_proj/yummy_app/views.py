from django.http import HttpResponse

from django.shortcuts import render, redirect
from . import models


# Create your views here.

def home(request):
    return  render(request,'home.html')

def category(request, category):
    context = {
        "categoryName": category,
        "All_Dishes": models.getCategoryByName(category),
        "Number": 3,
    }
    return render(request, "categories.html", context)


def cart(request):
    return render(request, "cart.html")


def addToCart(request, category):
    if request.method == "POST":
        user_id = request.session["id"]
        dishToAdd = request.POST["dishToAdd"]
        models.addToCart(user_id, dishToAdd)
        return redirect("/addToCart/" + category)
    else:
        return HttpResponse("You aren't allowed to manually modify the URL!")


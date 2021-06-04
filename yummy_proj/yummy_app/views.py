from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import models


# Create your views here.

def home(request):
    request.session['id'] = 1
    return render(request, 'home.html')


def category(request, category):
    context = {
        "categoryName": category,
        "All_Dishes": models.getCategoryByName(category),
        "Number": 3,
    }
    return render(request, "categories.html", context)


def cart(request):
    user_id = request.session['id']
    context = {
        'items': models.getAllInCart(user_id)
    }
    return render(request, "cart.html", context)


def addToCart(request, category):
    if request.method == "POST":
        user_id = request.session["id"]
        dishToAdd = request.POST["dishToAdd"]
        user = models.getuserby_id(int(user_id))
        if user is not None:
            models.addToCart(user, dishToAdd)
        return redirect("/yummy/" + category)
    else:
        return HttpResponse("You aren't allowed to manually modify the URL!")

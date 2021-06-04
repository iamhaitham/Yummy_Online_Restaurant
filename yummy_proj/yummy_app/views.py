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
    totalprice = 0
    items = models.getAllInCart(user_id)
    itemslist = []
    for item in items:
        itemslist.append(
            (item, models.getdishquantity(user_id, item), item.price * models.getdishquantity(user_id, item)))
        totalprice += item.price * models.getdishquantity(user_id, item)
    context = {
        'items': itemslist,
        'totalprice': totalprice
    }

    return render(request, "cart.html", context)


def addToCart(request, category):
    if request.method == "POST":
        user_id = request.session["id"]
        dishToAdd = request.POST["dishToAdd"]
        models.addToCart(int(user_id), dishToAdd)
        return redirect("/yummy/" + category)
    else:
        return HttpResponse("You aren't allowed to manually modify the URL!")


def removeFromCart(request, dishid):
    user_id = request.session['id']
    models.removedish(user_id, dishid)
    totalprice = 0
    items = models.getAllInCart(user_id)
    itemslist = []
    for item in items:
        itemslist.append(
            (item, models.getdishquantity(user_id, item), item.price * models.getdishquantity(user_id, item)))
        totalprice += item.price * models.getdishquantity(user_id, item)
    context = {
        'items': itemslist,
        'totalprice': totalprice
    }

    return render(request, 'cart_update.html', context)


def updateqty(request, id):
    cartdishobj = models.Cartdish.objects.filter(dish=models.getdishby_id(id))
    if cartdishobj != {}:
        cartdishobj.update(quantity=int(request.GET['quantity']))
    user_id = request.session['id']
    totalprice = 0
    items = models.getAllInCart(user_id)
    itemslist = []
    for item in items:
        itemslist.append(
            (item, models.getdishquantity(user_id, item), item.price * models.getdishquantity(user_id, item)))
        totalprice += item.price * models.getdishquantity(user_id, item)
    context = {
        'items': itemslist,
        'totalprice': totalprice
    }
    return render(request, 'cartupdate_qty.html', context)

import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import models


# Create your views here.

def home(request):
    if 'loggedin' not in request.session:
        request.session['id'] = 0
    user_id = request.session['id']
    if models.havecart(user_id) is None:
        models.createcart(user_id)

    return render(request, 'home.html')


def category(request, category):
    namelist = []
    for item in models.getCategoryByName(category):
        namelist.append(item.name)
    json_list = json.dumps(namelist)

    context = {
        "categoryName": category,
        "All_Dishes": models.getCategoryByName(category),
        "Number": 3,
        "namelist": json_list,
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
        if 'qty' in request.POST:
            qty = int(request.POST['qty'])
            models.addToCart(int(user_id), dishToAdd, qty)
        else:
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


def info(request, id):
    context = {
        "dish": models.InfoById(id=id)
    }
    return render(request, "info.html", context)


def searchdish(requset, phrase):
    namelist = []
    categoryname = requset.GET['category']
    for item in models.searchdishes(phrase, categoryname):
        namelist.append(item.name)
    json_list = json.dumps(namelist)

    context = {
        "All_Dishes": models.searchdishes(phrase, categoryname),
        "namelist": json_list,
    }
    return render(requset, "categories_update.html", context)


def resetsearch(request):
    categoryname = request.GET['category']
    namelist = []
    for item in models.getCategoryByName(categoryname):
        namelist.append(item.name)
    json_list = json.dumps(namelist)

    context = {
        "categoryName": categoryname,
        "All_Dishes": models.getCategoryByName(categoryname),
        "Number": 3,
        "namelist": json_list,
    }
    return render(request, "categories_update.html", context)

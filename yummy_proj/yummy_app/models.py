from django.db import models
from django.db.models import F

from login_register_app.models import User


# TODO Fix imports

class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # dishes=
    # restaurants=


class Restaurant(models.Model):
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    website = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, related_name="restaurants")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Dish(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name="dishes", on_delete=models.CASCADE)
    image = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    home = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    quantity = models.IntegerField()
    note = models.TextField()
    grand_total = models.FloatField()
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    location = models.OneToOneField(Location, related_name="order", on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    dish = models.ManyToManyField(Dish, through='cartdish')
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cartdish(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


def getCategoryByName(category):
    category = Category.objects.get(name=category)
    return category.dishes.all()

def getdishby_id(dishid):
    try:
        dish = Dish.objects.get(id=dishid)
    except Exception as e:
        print("Error getting Dish from database", e)
        return None
    return dish


def getuserby_id(user_id):
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        print("Error getting uer from database", e)
        return None
    return user


def addToCart(user, dishToAdd):
    dish = getdishby_id(dishToAdd)
    user = getuserby_id(user)
    if user is not None and dish is not None:

        cartdish, created = Cartdish.objects.get_or_create(dish=dish, cart=user.cart)
        if not created:
            cartdish.quantity = F('quantity') + 1
            cartdish.save(update_fields=["quantity"])
    else:
        print("Error adding to cart")


def getAllInCart(user_id):
    user = getuserby_id(user_id)
    if user is not None:
        return user.cart.dish.all()
    return []


def removedish(user_id, dishid):
    dish = getdishby_id(dishid)
    user = getuserby_id(user_id)
    if user is not None and dish is not None:
        user.cart.dish.remove(dish)
    else:
        print("Error deleting dish from cart")


def getdishquantity(user_id, dish):
    user = getuserby_id(user_id)
    cart = user.cart
    if user is not None and cart is not None:
        return dish.cartdish_set.get(cart=cart).quantity
    return 1
  
def InfoById(id):
    dish=Dish.objects.get(id=id)
    return dish

from django.db import models

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
    image=models.TextField(null=True)
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
    dish = models.ManyToManyField(Dish, related_name="carts")
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def getCategoryByName(category):
    category=Category.objects.get(name=category)
    return category.dishes.all()

def addToCart(user_id,dishToAdd):
    cart=Cart.objects.create(user=user_id)
    cart.dish.add(dishToAdd)
    
    
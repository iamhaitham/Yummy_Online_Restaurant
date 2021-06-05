from django.contrib import admin

# Register your models here.
from yummy_app.models import *


@admin.register(Dish)
class Dish(admin.ModelAdmin):
    pass


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    pass


@admin.register(Order)
class Order(admin.ModelAdmin):
    pass


@admin.register(Location)
class Location(admin.ModelAdmin):
    pass


@admin.register(Restaurant)
class Restaurant(admin.ModelAdmin):
    pass


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

@admin.register(Cartdish)
class Cartdish(admin.ModelAdmin):
    pass

from django.urls import path

from . import views

urlpatterns = [

    path('', views.home),
    path('<category>', views.category),
    path('cart/cart', views.cart),
    #TODO fix this route to soemthing like /yummy/cart
    #TODO fix the <category> route so its soemthing like /catelog/<Category>

]

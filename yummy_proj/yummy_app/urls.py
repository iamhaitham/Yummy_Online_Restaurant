from django.urls import path

from . import views

urlpatterns = [

    path('', views.home),
    path('<category>', views.category),
    path('cart/cart', views.cart),
    path('addToCart/<category>', views.addToCart),
    path('removeFromCart/<dishid>', views.removeFromCart),
    path('update/<id>', views.updateqty),
    path('info/info/<int:id>', views.info),
    path('search/<str:phrase>', views.searchdish),

    # TODO fix this route to soemthing like /yummy/cart
    # TODO fix the <category> route so its soemthing like /catelog/<Category> 
]

from django.urls import path

from . import views

urlpatterns = [

    path('', views.home),
    path('catalog/<category>', views.category),
    path('cart', views.cart),
    path('addToCart/<category>', views.addToCart),
    path('removeFromCart/<dishid>', views.removeFromCart),
    path('update/<id>', views.updateqty),
    path('info/<int:id>', views.info),
    path('search/<str:phrase>', views.searchdish),
    path('searchreset/', views.resetsearch),
    path('orders', views.orders),
    path('contactus', views.contactus),

    ################################################
    ################################################
    # EDITED THE URLS ABOVE SO THEY ARE
    # CONVENIENT WITH EVERYWHERE THEY ARE CALLED
    ################################################
    ################################################

    # TODO fix this route to soemthing like /yummy/cart
    # TODO fix the <category> route so its soemthing like /catelog/<Category> 
]

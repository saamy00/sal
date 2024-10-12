from django.contrib import admin
from django.urls import path
from .views import product_list,add_to_cart,view_cart,headphone,laptop,remove_from_cart
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',product_list,name='product_list'),
    path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('view_cart/',view_cart,name='view_cart'),
    path('headphone/',headphone,name='headphone'),
    path('laptop/',laptop,name='laptop'),
    path('remove_from_cart/<int:cart_item_id>/',remove_from_cart,name='remove_from_cart'),
]
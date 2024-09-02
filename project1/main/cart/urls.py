from django.urls import path ,include
from .import views

urlpatterns = [
    path('',views.cart_summray,name="cart_summary"),
    path('add/',views.add_cart,name="add_cart"),
    path('update/',views.update_cart,name="update_cart"),
    path('delete/',views.delete_cart,name="delete_cart"),
    
]

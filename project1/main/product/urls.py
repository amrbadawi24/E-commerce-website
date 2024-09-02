from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.product_all,name="products"),
    path('product/<int:pk>/', views.product_page, name="product"),
    path('search/',views.search,name="search"),
    path('category/<str:n>/', views.category_all, name="category"),
]
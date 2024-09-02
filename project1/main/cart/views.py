from django.shortcuts import render,redirect,get_object_or_404
from .cart import Cart
from django.contrib import messages
from product.models import product
from django.http import JsonResponse


# Create your views here.
def cart_summray(request):
    cart = Cart(request)
    cart_products=cart.get_prods
    qty=cart.get_quants
    totals=cart.cart_total()
    return render(request,'cart/cart_summary.html',{"product_list": cart_products ,'quants':qty,'total': totals})
def add_cart(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')
        prod=get_object_or_404(product, id=product_id)
        cart.add(prod,product_qty)
        cart_num=cart.__len__()
        
        response = JsonResponse({'qty': cart_num})
        return response
    
def update_cart(request):
    pass
def delete_cart(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        return response

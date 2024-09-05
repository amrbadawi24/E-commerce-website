from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from cart.cart import Cart
from cart.views import *
from django.contrib.auth.models import User
from .forms import *
from product.models import product
from .models import *
# Create your views here.

@login_required
def not_shipped_dash(request):
    if request.user.is_superuser:
        orders=order.objects.filter(shipped=False).order_by('-date_orderd') 
        return render(request,'payment/shipped_dash.html',{'orders':orders})
    orders=order.objects.filter(user=request.user)
    return render(request,'payment/shipped_dash.html',{'orders':orders})


@login_required
def shipped_dash(request):
    if request.user.is_superuser:
        orders=order.objects.filter(shipped=True).order_by('-date_orderd') 
        return render(request,'payment/shipped_dash.html',{'orders':orders})
    orders=order.objects.filter(user=request.user)
    return render(request,'payment/shipped_dash.html',{'orders':orders})


def order_page(request,pk):
    try:
        orderr=order.objects.get(id=pk)
    except order.DoesNotExist:
        return redirect('home')
    items=order_item.objects.filter(order=pk)
    one_hour_ago = timezone.now() - timezone.timedelta(minutes=60)
    if request.method == 'POST':
        if 'delete_order' in request.POST:
            orderr.delete()
            messages.success(request, 'Order Deleted!')
            return redirect('home')
        elif request.method == 'POST' and orderr.shipped==False:
            orderr.shipped = True
            orderr.save()
            messages.success(request, 'Order marked as shipped!')
            return redirect('home')
        elif request.method == 'POST' and  orderr.shipped==True:
            orderr.shipped = False
            orderr.save()
            messages.success(request, 'Order marked as Un shipped!')
            return redirect('home')
    return render(request,'payment/order_page.html',{'orders':orderr,'items':items, 'one_hour_ago': one_hour_ago})


@login_required
def process_order(request):
    if request.POST:
        payment_form=paymentform(request.POST or None)
        cart = Cart(request)
        cart_products=cart.get_prods()
        qty=cart.get_quants()
        totals=cart.cart_total()
        shipping_address1 = shippingaddress.objects.get(user=request.user)
        
        #fill in the order model how we get all the info from before 
        
        user = request.user
        full_name = user.first_name + ' ' + user.last_name
        shipping_adress_of_user =f"User: {shipping_address1.user},\n Full name: {shipping_address1.full_name},\n Address: {shipping_address1.address1},\n phone number: {shipping_address1.phone_number},\n country: {shipping_address1.country},\n state: {shipping_address1.state},\n city: {shipping_address1.city}"
        amount_paid = totals
        
        #create an order
        create_order=order(user=user , full_name=full_name , shipping_address=shipping_adress_of_user , amount_paid=totals)
        create_order.save()      
        
        #add order items 
        order_id=create_order.pk
        
        for product in cart_products:
            product_id = product.id
            price = product.price
            for key, value in qty.items():
                if int(key) == product_id:
                    create_order_item = order_item(
                        order_id=order_id,
                        product_id=product_id,
                        user_id=user.id,
                        quantity=value,
                        price=price
                    )
                    create_order_item.save()
        
        messages.success(request, 'Order Created successfuly!')
        return redirect('home')
    else:
        message.succsess(request,'acsess denied')
        return redirect('home')


@login_required
def billing_info(request):
    billing_form = paymentform()
    return render(request,"payment/billing_info.html",{'form': billing_form})


@login_required
def check_out(request):
    cart = Cart(request)
    cart_products=cart.get_prods
    qty=cart.get_quants
    totals=cart.cart_total()
    try:
        shipping_address = shippingaddress.objects.get(user=request.user)
    except shippingaddress.DoesNotExist:
        return redirect('create_shipping')
    return render(request,'payment/check_out.html',{"product_list": cart_products ,'quants':qty,'total': totals,'shipping_address':shipping_address})


@login_required
def create_shipping(request):
    if request.method == 'POST':
        form = shippingform(request.POST)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.user = request.user
            shipping_address.save() 
            messages.success(request, 'You have Created your shipping form successfully!')
            return redirect('update_shipping')
    else:
        form = shippingform()
    return render(request, 'payment/create_shipping.html', {'form': form})

@login_required
def update_shipping(request):
    try:
        shipping_address = shippingaddress.objects.get(user=request.user)
    except shippingaddress.DoesNotExist:
        return redirect('create_shipping')

    if request.method == 'POST':
        form = shippingform(request.POST, instance=shipping_address)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have Updated your shipping form successfully!')
            return redirect('update_shipping')
    else:
        form = shippingform(instance=shipping_address)
    return render(request, 'payment/update_shipping.html', {'form': form})
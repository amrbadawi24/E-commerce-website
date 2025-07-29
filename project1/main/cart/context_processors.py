from .cart import Cart

# do this so that cart is availble evreywhere in our site 

def cart(request):
    return{'cart':Cart(request)}
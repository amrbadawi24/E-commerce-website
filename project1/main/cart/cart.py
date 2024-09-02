from product.models import product

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.session_key = 'cart'
        if self.session_key not in self.session:
            self.session[self.session_key] = {}
        self.cart = self.session[self.session_key]
            
    def add(self,product,qty):
        product_id = str(product.id)
        product_qty= str(qty)
        if product_id in self.session[self.session_key]:
            pass
        else:
            self.session[self.session_key][product_id] = int(product_qty)

            
        self.session.modified = True
        
    def __len__(self):
        return len(self.cart)
        
    def cart_total(self):
        product_ids = self.cart.keys()
        products = product.objects.filter(id__in=product_ids)
        quant = self.cart
        total = 0
        for key, value in quant.items():  # Call the items() method
            key = int(key)
            for prod in products:
                if prod.id == key:
                    total = total + (prod.price * value)
        return total
    
    
    def get_prods(self):
        product_ids =self.cart.keys()
        products = product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantities=self.cart
        return quantities
    
    def delete(self,product):
        product_id=str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified=True
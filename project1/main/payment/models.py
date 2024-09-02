from django.db import models
from django.contrib.auth.models import User
from product.models import product
# Create your models here.

class shippingaddress(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True ,unique=True)
    full_name=models.CharField(max_length=255)
    address1=models.CharField(max_length=255)
    phone_number=models.DecimalField(max_digits=20,decimal_places=0)
    country=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    city=models.CharField(max_length=255) 
    
    def __str__(self):
        return f" shipping adress of : {str(self.id)}"
    
class order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    full_name=models.CharField(max_length=255)
    shipping_address=models.TextField()
    shipped=models.BooleanField(default=False)
    amount_paid=models.DecimalField(max_digits=10 ,decimal_places=2)
    date_orderd=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f" order : {str(self.id)}"
    
class order_item(models.Model):
    order = models.ForeignKey(order , on_delete=models.CASCADE , null=True , blank=True )
    product = models.ForeignKey(product , on_delete=models.CASCADE , null=True , blank=True )
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True )
    
    quantity=models.PositiveIntegerField(default=1)
    price= models.DecimalField(max_digits = 10 ,decimal_places=2)
    
    def __str__(self):
        return f" order : {str(self.id)}"

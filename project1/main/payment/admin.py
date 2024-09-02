from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(shippingaddress)
admin.site.register(order)
admin.site.register(order_item)
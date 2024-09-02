from django.contrib import admin
from .models import product ,comments , category


class ProductAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
    
# Register your models here.
admin.site.register(product,ProductAdmin)

admin.site.register(category)

admin.site.site_header ='Product manegment' 
admin.site.site_title ="Admin manegment"

admin.site.register(comments)


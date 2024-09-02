from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='product/%y%m%d')
    content = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        
class comments(models.Model):
    Id = models.ForeignKey('product', to_field='id', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_add=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_add']
    

    

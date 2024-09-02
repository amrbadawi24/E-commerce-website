from django.shortcuts import render , redirect
from django.contrib import messages
from product.models import product

# Create your views here.

def home_page(request):
    g = product.objects.all().order_by("-created_at")[:6]
    return render(request, 'home/home.html', {'products': g})

from django.shortcuts import render, get_object_or_404, redirect
from .models import product , comments,category
from .forms import commentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.'
def product_all(request):
    pro = product.objects.all()
    sort_by = request.GET.get('sort_by', '-created_at')
    pro = pro.order_by(sort_by)
    p = Paginator(pro, 12)
    page = request.GET.get('page')
    prod = p.get_page(page)
    return render(request, 'product/products.html', {"product_list": prod, "sort_by": sort_by})

@login_required
def product_page(request, pk):
    g = product.objects.get(id=pk)
    c = comments.objects.filter(Id=g).order_by('-date_add')  # Fetch comments for the specific product and order them by date

    if request.method == 'POST':
        comment_form = commentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.Id = g
            comment.name = request.user  # Assign the logged-in user as the commenter
            comment.save()
            return redirect('product', pk=pk)
        else:
            return redirect('product', pk=pk)
    
    comment_form = commentForm()
    return render(request, 'product/product.html', {"product_list": g, "comment_list": c, "comment_form": comment_form})

def category_all(request, n):
    cat = category.objects.get(name=n)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    products = product.objects.filter(category=cat)
    if min_price and max_price:
        min_price = float(min_price)
        max_price = float(max_price)
        products = products.filter(price__range=(min_price, max_price))
    p = Paginator(products,12)
    page = request.GET.get('page')
    prod=p.get_page(page)
    return render(request, 'product/category.html', {'products_list': prod, 'category': cat})


def search(request):
    if request.method == "GET":
        searched = request.GET.get('search')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if searched:
            g = product.objects.filter(name__icontains=searched)
            if min_price and max_price:
                min_price = float(min_price)
                max_price = float(max_price)
                g = g.filter(price__range=(min_price, max_price))

            p = Paginator(g, 12)
            page = request.GET.get('page')
            prod = p.get_page(page)
            return render(request, 'product/search.html', {"product_list": prod})
        else:
            search_notfind = "no content found"
            return render(request, 'product/search.html', {'not_found': search_notfind})
    return render(request, 'product/search.html')
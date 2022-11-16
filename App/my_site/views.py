from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView


def product_list_view(request):
    """redirect to catalogue"""
    products = Product.objects.all()
    return render(request, 'my_site/catalogue.html', {
        'products': products,
    })


def gallery_page(request):
    """redirect to gallery page"""
    return render(request, 'my_site/gallery.html')


def contacts_page(request):
    """redirect to contacts page"""
    return render(request, 'my_site/contacts.html')


def news_page(request):
    """redirect to news page"""
    return render(request, 'my_site/news.html')


def about_page(request):
    """redirect to news page"""
    return render(request, 'my_site/about.html')


def home_page(request):
    """return to home page"""
    return render(request, 'my_site/home.html')


def detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'my_site/detail.html', {
        'product': product,
    })

from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Cart, Entry


def view_cart(request: HttpRequest):
    if not request.session._session_key:
        print("Creating session and cart")
        request.session.create()
        request.session.set_expiry(None)
        Cart.objects.create(user=request.session.session_key)
        print("created")
    my_cart, created = Cart.objects.get_or_create(user=request.session._session_key)
    list_of_entries = list(set(Entry.objects.filter(cart=my_cart)))
    template = 'my_site/cart.html'

    return render(request, template, {
        'cart': list_of_entries,
        'my_cart': my_cart,
    })

@transaction.atomic
def add_cart_item(request, pk):
    if not request.session._session_key:
        print("Creating session and cart")
        request.session.create()
        request.session.set_expiry(None)
        Cart.objects.create(user=request.session.session_key)
        print("created")
    product = Product.objects.filter(id=pk).first()
    quantity = request.POST.get('quantity')
    my_cart, created = Cart.objects.get_or_create(user=request.session._session_key)
    Entry.objects.filter(product=product, cart=my_cart).delete()
    entry1 = Entry.objects.get_or_create(product=product, cart=my_cart, quantity=int(quantity))
    add_cart_item_notify(request, pk, quantity)


def add_cart_item_notify(request, pk, quantity):
    product = get_object_or_404(Product, id=pk)
    messages.success(request, f"{product.name} - {quantity}шт. успешно добавлено")
def delete_cart_item(request, pk):
    product = Product.objects.filter(id=pk).first()
    my_cart = Cart.objects.filter(user=request.session._session_key).first()
    Entry.objects.filter(product=product, cart=my_cart).delete()

    my_cart, created = Cart.objects.get_or_create(user=request.session._session_key)
    list_of_entries = list(set(Entry.objects.filter(cart=my_cart)))
    template = 'my_site/cart.html'

    return render(request, template, {
        'cart': list_of_entries,
        'my_cart': my_cart,
    })

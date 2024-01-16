from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from products.models import Product


def increase_item_in_cart_quantity(request):
    product_id = request.GET.get('id')
    is_catalog = request.GET.get('is_catalog')
    page = request.GET.get('page')
    if product_id:
        cart = request.session.get('cart') or {}
        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1
        request.session['cart'] = cart
    if is_catalog:
        return redirect(reverse('products:products_list') + f'?page={page}')
    return redirect(reverse('cart:products_in_cart_list'))


def decrease_item_in_cart_quantity(request):
    product_id = request.GET.get('id')
    is_catalog = request.GET.get('is_catalog')
    page = request.GET.get('page')
    if product_id:
        cart = request.session.get('cart') or {}
        if product_id in cart:
            if is_catalog and cart[product_id] == 1:
                cart.pop(product_id)
            elif cart[product_id] > 0:
                cart[product_id] -= 1
        request.session['cart'] = cart
    if is_catalog:
        return redirect(reverse('products:products_list') + f'?page={page}')
    return redirect(reverse('cart:products_in_cart_list'))


def remove_item_in_cart(request):
    product_id = request.GET.get('id')
    if product_id:
        cart = request.session.get('cart') or {}
        cart.pop(product_id)
        request.session['cart'] = cart
    return redirect(reverse('cart:products_in_cart_list'))


def clear_item_in_cart(request):
    cart = request.session.get('cart') or {}
    cart.clear()
    request.session['cart'] = cart
    return redirect(reverse('cart:products_in_cart_list'))


def submit_order(request):
    cart = request.session.get('cart') or {}
    cart.clear()
    request.session['cart'] = cart
    return redirect(reverse('products:products_list') + '?is_submitted=True')


def cart_view(request):
    cart_items = []
    total = 0
    if request.method == 'GET':
        cart = request.session.get('cart') or {}
        for product_id, product_quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            cart_item_total = product.price * product_quantity
            total += cart_item_total
            cart_items.append({'product': product, 'quantity': product_quantity, 'item_total': cart_item_total})
    return render(request, 'products_in_cart_list.html',
                  {'is_empty': len(cart_items) == 0, 'cart_items': cart_items, 'total': total})

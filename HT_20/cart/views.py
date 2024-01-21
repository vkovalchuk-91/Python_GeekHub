from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from products.models import Product


@login_required
def increase_item_in_cart_quantity(request, pk):
    product_id = str(pk)
    cart = request.session.get('cart') or {}
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', reverse('products:products_list')))


@login_required
def decrease_item_in_cart_quantity(request, pk):
    product_id = str(pk)
    cart = request.session.get('cart') or {}
    if product_id in cart:
        is_cart = str(request.META.get('HTTP_REFERER', 'not_cart'))[-5:] == 'cart/'
        if not is_cart and cart[product_id] == 1:
            cart.pop(product_id)
        elif cart[product_id] > 0:
            cart[product_id] -= 1
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', reverse('products:products_list')))


@login_required
def remove_item_in_cart(request, pk):
    product_id = str(pk)
    if product_id:
        cart = request.session.get('cart') or {}
        cart.pop(product_id)
        request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', reverse('products:products_list')))


@login_required
def clear_item_in_cart(request):
    cart = request.session.get('cart') or {}
    cart.clear()
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', reverse('products:products_list')))


@login_required
def submit_order(request):
    cart = request.session.get('cart') or {}
    cart.clear()
    request.session['cart'] = cart
    messages.success(request, 'Замовлення прийнято в обробку.')
    return redirect(reverse('products:products_list'))


@login_required
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

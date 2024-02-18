from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from products.models import Product


@login_required
def ajax_change_quantity(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        item_price = request.POST.get('price')
        item_cost_current = request.POST.get('item-cost')
        total_cost_current = request.POST.get('total-cost')
        cart = request.session.get('cart') or {}

        is_cart = str(request.META.get('HTTP_REFERER', 'not_cart'))[-5:] == 'cart/'
        if action == 'increase':
            if product_id in cart:
                cart[product_id] += 1
            else:
                cart[product_id] = 1
        elif action == 'decrease' and product_id in cart:
            if not is_cart and cart[product_id] == 1:
                cart.pop(product_id)
                request.session['cart'] = cart
                return JsonResponse({})
            elif cart[product_id] > 0:
                cart[product_id] -= 1

        request.session['cart'] = cart

        if is_cart:
            item_cost_updated = round(cart[product_id] * float(item_price), 2)
            total_cost_updated = round(float(total_cost_current) - float(item_cost_current) + item_cost_updated, 2)
            return JsonResponse({'quantity': cart[product_id], 'cost': item_cost_updated, 'total': total_cost_updated})
        else:
            return JsonResponse({'quantity': cart[product_id]})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def ajax_remove_item(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        item_cost_current = request.POST.get('item-cost')
        total_cost_current = request.POST.get('total-cost')

        cart = request.session.get('cart') or {}
        cart.pop(str(product_id))
        request.session['cart'] = cart

        total_cost_updated = round(float(total_cost_current) - float(item_cost_current), 2)
        return JsonResponse({'total': total_cost_updated})

    if request.method == 'DELETE':
        cart = request.session.get('cart') or {}
        cart.clear()
        request.session['cart'] = cart
        return JsonResponse({})

    return JsonResponse({'error': 'Invalid request'}, status=400)


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

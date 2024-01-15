from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic import DetailView

from .forms import GetProductIdsForm
from .models import Product
from .services import handle_valid_data


def product_input(request):
    success_message = None

    if request.method == 'POST':
        form = GetProductIdsForm(request.POST)
        if form.is_valid():
            handle_valid_data(form.cleaned_data)
            success_message = 'Дані успішно додані в чергу на обробку!'
        else:
            success_message = "Дозволені тільки латинські букви, цифри та кома!"

    form = GetProductIdsForm()
    return render(request, 'product_input.html', {'form': form, 'success_message': success_message})


class ProductsListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products_list"
    paginate_by = 10
    ordering = ['-update_date']


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product_details"


def add_to_cart(request):
    product_id = request.GET.get('id')
    page = request.GET.get('page')
    if product_id:
        cart = request.session.get('cart') or {}
        if product_id in cart:
            cart.pop(product_id)
        else:
            cart[product_id] = 1
        request.session['cart'] = cart
    return redirect(reverse('products:products_list') + f'?page={page}')


def increase_item_in_cart_quantity(request):
    product_id = request.GET.get('id')
    if product_id:
        cart = request.session.get('cart') or {}
        if product_id in cart:
            cart[product_id] += 1
        request.session['cart'] = cart
    return redirect(reverse('products:products_in_cart_list'))


def decrease_item_in_cart_quantity(request):
    product_id = request.GET.get('id')
    if product_id:
        cart = request.session.get('cart') or {}
        if product_id in cart:
            if cart[product_id] > 0:
                cart[product_id] -= 1
        request.session['cart'] = cart
    return redirect(reverse('products:products_in_cart_list'))


def remove_item_in_cart(request):
    product_id = request.GET.get('id')
    if product_id:
        cart = request.session.get('cart') or {}
        cart.pop(product_id)
        request.session['cart'] = cart
    return redirect(reverse('products:products_in_cart_list'))


def clear_item_in_cart(request):
    cart = request.session.get('cart') or {}
    cart.clear()
    request.session['cart'] = cart
    return redirect(reverse('products:products_in_cart_list'))


def submit_order(request):
    cart = request.session.get('cart') or {}
    cart.clear()
    request.session['cart'] = cart
    return redirect(reverse('products:products_list') + '?is_submitted=True')


def cart_view(request):
    cart_items = []
    total = 0
    if request.method == 'GET':
        cart = request.session.get('cart')
        for product_id, product_quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            cart_item_total = product.price * product_quantity
            total += cart_item_total
            cart_items.append((product, product_quantity, cart_item_total))
    return render(request, 'products_in_cart_list.html',
                  {'is_empty': len(cart_items) == 0, 'cart_items': cart_items, 'total': total})

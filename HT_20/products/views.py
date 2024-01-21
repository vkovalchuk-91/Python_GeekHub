from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic import DetailView

from .forms import GetProductIdsForm, ProductForm
from .models import Product, Category
from .services import handle_valid_data


def product_input(request):
    if request.user and not request.user.is_superuser:
        messages.error(request, 'Доступ до сторінки додавання нових продуктів мають лише суперюзери.')
        return redirect(reverse('products:products_list'))

    if request.method == 'POST':
        form = GetProductIdsForm(request.POST)
        if form.is_valid():
            handle_valid_data(form.cleaned_data)
            messages.success(request, 'Дані успішно додані в чергу на обробку!')
        else:
            messages.error(request, 'Дозволені тільки латинські букви, цифри та кома!')

    form = GetProductIdsForm()
    return render(request, 'product_input.html', {'form': form})


class ProductsListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products_list"
    paginate_by = 10
    ordering = ['-update_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('cat_slug')
        if category_slug:
            queryset = queryset.filter(category_id=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart') or {}
        items = []
        for product in context['object_list']:
            product_id = str(product.pk)
            quantity = cart[product_id] if product_id in cart.keys() else 0
            items.append({'product': product, 'quantity': quantity})
        context['items_list'] = items
        context['categories'] = Category.objects.all()
        filtered_category = Category.objects.filter(id=self.kwargs.get('cat_slug')).first()
        if filtered_category:
            filtered_category_label = filtered_category.name
        else:
            filtered_category_label = 'Всі категорії'
        context['filtered_category'] = filtered_category_label
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product_details"


def product_edit(request, pk):
    if request.user and not request.user.is_superuser:
        messages.error(request, 'Доступ до сторінки редагування продуктів мають лише суперюзери.')
        return redirect(reverse('products:products_list'))

    edit_object = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=edit_object)
        if form.is_valid():
            form.save()
            messages.success(request, f'Дані продукта ID={pk} були успішно збережені.')
            return redirect(reverse('products:products_list'))
        else:
            messages.error(request, f'Введено невалідні дані. Повторіть спробу!')

    form = ProductForm(instance=edit_object)
    return render(request, 'product_edit.html', {'form': form, 'pk': pk})


def product_update_from_sears_com(request, pk):
    if request.user and not request.user.is_superuser:
        messages.error(request, 'Доступ до сторінки оновлення продуктів мають лише суперюзери.')
        return redirect(reverse('products:products_list'))

    edit_object = get_object_or_404(Product, pk=pk)
    handle_valid_data({'ids_raw_data': edit_object.product_id})
    messages.success(request, 'Дані успішно додані в чергу на оновлення!')
    return redirect(reverse('products:products_list'))


def product_delete(request, pk):
    if request.user and not request.user.is_superuser:
        messages.error(request, 'Доступ до сторінки видалення продуктів мають лише суперюзери.')
        return redirect(reverse('products:products_list'))

    delete_object = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        if request.POST.get('confirm_delete'):
            delete_object.delete()
            messages.success(request, f'Продукт ID={pk} був успішно видалений.')
            return redirect(reverse('products:products_list'))

    page = request.GET.get('page')
    return render(request, 'product_delete.html', {'delete_object': delete_object, 'page': page})

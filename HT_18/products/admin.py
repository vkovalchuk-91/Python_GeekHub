from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'price', 'update_date')


admin.site.register(Product, ProductAdmin)

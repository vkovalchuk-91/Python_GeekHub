from django.urls import path

from . import views
from .views import add_to_cart
from .views import increase_item_in_cart_quantity
from .views import decrease_item_in_cart_quantity
from .views import remove_item_in_cart
from .views import clear_item_in_cart
from .views import submit_order

app_name = "products"
urlpatterns = [
    path("", views.product_input, name="product_input"),
    path("products", views.ProductsListView.as_view(), name="products_list"),
    path("product/<int:pk>", views.ProductDetailView.as_view(), name="product_details"),
    path("cart", views.cart_view, name="products_in_cart_list"),
    path("add_to_cart", add_to_cart, name="add_to_cart"),
    path("increase_item_in_cart_quantity", increase_item_in_cart_quantity, name="increase_item_in_cart_quantity"),
    path("decrease_item_in_cart_quantity", decrease_item_in_cart_quantity, name="decrease_item_in_cart_quantity"),
    path("remove_item_in_cart", remove_item_in_cart, name="remove_item_in_cart"),
    path("clear_item_in_cart", clear_item_in_cart, name="clear_item_in_cart"),
    path("clear_item_in_cart", clear_item_in_cart, name="clear_item_in_cart"),
    path("submit_order", submit_order, name="submit_order"),
]

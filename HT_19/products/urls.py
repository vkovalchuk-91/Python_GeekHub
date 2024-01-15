from django.urls import path

from .views import product_input
from .views import ProductsListView
from .views import ProductDetailView
from .views import cart_view
from .views import add_to_cart
from .views import increase_item_in_cart_quantity
from .views import decrease_item_in_cart_quantity
from .views import remove_item_in_cart
from .views import clear_item_in_cart
from .views import submit_order

app_name = "products"
urlpatterns = [
    path("", product_input, name="product_input"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("cart/", cart_view, name="products_in_cart_list"),
    path("cart/add/", add_to_cart, name="add_to_cart"),
    path("cart/quantity/increase/", increase_item_in_cart_quantity, name="increase_item_in_cart_quantity"),
    path("cart/quantity/decrease/", decrease_item_in_cart_quantity, name="decrease_item_in_cart_quantity"),
    path("cart/remove/", remove_item_in_cart, name="remove_item_in_cart"),
    path("cart/clear/", clear_item_in_cart, name="clear_item_in_cart"),
    path("cart/submit/", submit_order, name="submit_order"),
]

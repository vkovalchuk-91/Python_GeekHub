from django.urls import path

from .views import cart_view
from .views import increase_item_in_cart_quantity
from .views import decrease_item_in_cart_quantity
from .views import remove_item_in_cart
from .views import clear_item_in_cart
from .views import submit_order

app_name = "cart"
urlpatterns = [
    path("", cart_view, name="products_in_cart_list"),
    path("quantity/increase/", increase_item_in_cart_quantity, name="increase_item_in_cart_quantity"),
    path("quantity/decrease/", decrease_item_in_cart_quantity, name="decrease_item_in_cart_quantity"),
    path("remove/", remove_item_in_cart, name="remove_item_in_cart"),
    path("clear/", clear_item_in_cart, name="clear_item_in_cart"),
    path("submit/", submit_order, name="submit_order"),
]

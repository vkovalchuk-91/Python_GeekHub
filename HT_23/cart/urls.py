from django.urls import path

from .views import cart_view
from .views import ajax_change_quantity
from .views import ajax_remove_item
from .views import submit_order

app_name = "cart"
urlpatterns = [
    path("", cart_view, name="products_in_cart_list"),
    path('ajax_change_quantity/', ajax_change_quantity, name='ajax_change_quantity'),
    path('ajax_remove_item/', ajax_remove_item, name='ajax_remove_item'),
    path("submit/", submit_order, name="submit_order"),
]

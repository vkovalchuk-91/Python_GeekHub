from django.urls import path
from .api_views import CartListView

app_name = "api_cart"
urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart-api'),
]
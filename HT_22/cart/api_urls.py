from django.urls import path
from .api_views import CartListView

urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart-api'),
]
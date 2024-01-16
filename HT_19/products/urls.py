from django.urls import path

from .views import product_input
from .views import ProductsListView
from .views import ProductDetailView

app_name = "products"
urlpatterns = [
    path("", product_input, name="product_input"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
]

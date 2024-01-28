from django.urls import path

from .views import product_input
from .views import ProductsListView
from .views import ProductDetailView
from .views import product_edit
from .views import product_update_from_sears_com
from .views import product_delete

app_name = "products"
urlpatterns = [
    path("products/add/", product_input, name="product_input"),
    path("", ProductsListView.as_view(), name="products_list"),
    path("products/category_filter/<slug:cat_slug>/", ProductsListView.as_view(), name='products_list_by_category'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("products/edit/<int:pk>/", product_edit, name="product_edit"),
    path("products/update/<int:pk>/", product_update_from_sears_com, name="product_update_from_sears_com"),
    path("products/delete/<int:pk>/", product_delete, name="product_delete"),
]

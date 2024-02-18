from rest_framework import routers

from products import api_views

router = routers.DefaultRouter()
router.register(r'product', api_views.ProductViewSet)
router.register(r'category', api_views.CategoryViewSet)

app_name = "api_products"
urlpatterns = [
]

urlpatterns += router.urls

from django.urls import include, path
from rest_framework import routers

from products import api_views

router = routers.DefaultRouter()
router.register(r'product', api_views.ProductViewSet)
router.register(r'category', api_views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls

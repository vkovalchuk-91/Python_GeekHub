from rest_framework import viewsets, status
from rest_framework.response import Response

from products.models import Product, Category
from products.permissions import IsSuperuserOrReadOnly
from products.serializers import ProductSerializer, CategorySerializer, AddProductsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-update_date')
    serializer_class = ProductSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = AddProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                "success_message": "Data has been successfully added to the processing queue!",
                **serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserOrReadOnly]

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductSerializer
from .serializers import CartSerializer, CartUpdateSerializer, CartDeleteSerializer, CartAddSerializer


class CartListView(APIView):
    @staticmethod
    def get(request):
        serializer = CartListView.get_cart_api_content(request)
        return Response(serializer.data)

    @staticmethod
    def get_cart_api_content(request):
        cart_session_content = request.session.get('cart', {})
        cart_api_content = []
        for product_id, quantity in cart_session_content.items():
            product = get_object_or_404(Product, pk=product_id)
            product_serializer = ProductSerializer(product)
            cart_api_content.append({
                'product': product_serializer.data,
                'quantity': quantity
            })
        serializer = CartSerializer({'cart_items': cart_api_content})
        return serializer

    @staticmethod
    def post(request):
        serializer = CartAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data['product_id']

        cart = request.session.get('cart') or {}
        if str(product_id) in cart:
            return Response({"error": f"Product you want to add with id {product_id} is already in the cart."},
                            status=status.HTTP_400_BAD_REQUEST)
        cart[str(product_id)] = 1
        request.session['cart'] = cart
        request.session.modified = True

        serializer = CartListView.get_cart_api_content(request)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request):
        serializer = CartUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']

        cart = request.session.get('cart') or {}
        cart[str(product_id)] = quantity
        request.session['cart'] = cart
        request.session.modified = True

        serializer = CartListView.get_cart_api_content(request)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request):
        if request.data:
            serializer = CartDeleteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            product_id = serializer.validated_data['product_id']

            cart = request.session.get('cart') or {}
            if str(product_id) in cart:
                cart.pop(str(product_id))
                request.session['cart'] = cart
                request.session.modified = True
            else:
                return Response({"error": f"Product you want to delete with id {product_id} is no longer in the cart."},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            cart = request.session.get('cart') or {}
            if cart:
                cart.clear()
                request.session['cart'] = cart
                request.session.modified = True
            else:
                return Response({"error": f"The cart is already empty, there is nothing to delete."},
                                status=status.HTTP_400_BAD_REQUEST)

        serializer = CartListView.get_cart_api_content(request)
        return Response(serializer.data, status=status.HTTP_200_OK)

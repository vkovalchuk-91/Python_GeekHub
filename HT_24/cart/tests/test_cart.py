from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from products.tests.factories import UserFactory, ProductFactory


class CategoryTestCase(APITestCase):
    client = APIClient()
    maxDiff = None

    def setUp(self):
        self.products = ProductFactory.create_batch(7)
        self.user = UserFactory()

    def test_create_cart(self):
        response = self.add_cart_items(1, False)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised user

        response = self.add_cart_items(1, True)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)  # Authorised user
        self.assertEqual(response.data['cart_items'][0]['product']['id'], self.products[0].id)

        url = reverse('api_cart:cart-api')
        response_format = 'json'
        data = {'product_id': -1}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data=data, format=response_format)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.content)  # NonExisting adding
        self.assertEqual(response.data['product_id'][0],
                         "Product with this id does not exist.",
                         msg=response.content)

        response = self.add_cart_items(1, True)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.content)  # DuplicatedId adding
        self.assertEqual(response.data['error'],
                         f"Product you want to add with id {self.products[0].id} is already in the cart.",
                         msg=response.content)

    def test_retrieve_cart_items(self):
        items_in_cart = 3
        self.add_cart_items(items_in_cart, True)
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('api_cart:cart-api'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised user

        self.add_cart_items(items_in_cart, True)
        response = self.client.get(reverse('api_cart:cart-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)  # Authorised user
        self.assertEqual(len(response.data['cart_items']), items_in_cart, msg=response.content)

    def test_delete_cart_item(self):
        items_in_cart = 3
        url = reverse('api_cart:cart-api')
        data = {'product_id': self.products[0].id}
        response_format = 'json'
        self.add_cart_items(items_in_cart, True)
        self.client.force_authenticate(user=None)
        response = self.client.delete(url, data=data, format=response_format)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised user

        self.add_cart_items(items_in_cart, True)
        response = self.client.delete(url, data=data, format=response_format)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)  # Authorised user
        self.assertEqual(len(response.data["cart_items"]), items_in_cart - 1, msg=response.content)

        data = {'product_id': -1}
        response = self.client.delete(url, data=data, format=response_format)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST,
                         msg=response.content)  # NonExistingId deleting
        self.assertEqual(response.data['product_id'][0],
                         "Product with this id does not exist.",
                         msg=response.content)

    def test_put_cart_item(self):
        items_in_cart = 3
        url = reverse('api_cart:cart-api')
        updated_quantity = 5
        data = {'product_id': self.products[0].id, 'quantity': updated_quantity}
        response_format = 'json'
        self.add_cart_items(items_in_cart, True)
        self.client.force_authenticate(user=None)
        response = self.client.put(url, data=data, format=response_format)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised user

        self.add_cart_items(items_in_cart, True)
        response = self.client.put(url, data=data, format=response_format)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)  # Authorised user
        for cart_item in response.data['cart_items']:
            if cart_item["product"]['id'] == self.products[0].id:
                self.assertEqual(cart_item['quantity'], updated_quantity, msg=response.content)

        data = {'product_id': -1, 'quantity': updated_quantity}
        response = self.client.put(url, data=data, format=response_format)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST,
                         msg=response.content)  # NonExistingId put
        self.assertEqual(response.data['product_id'][0],
                         "Product with this id does not exist.",
                         msg=response.content)

        data = {'product_id': self.products[0].id, 'quantity': -1}
        response = self.client.put(url, data=data, format=response_format)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST,
                         msg=response.content)  # NonPositiveQuantity put
        self.assertEqual(response.data['quantity'][0],
                         "Quantity must be greater than 0.",
                         msg=response.content)

    def add_cart_items(self, item_numbers, is_authenticated):
        url = reverse('api_cart:cart-api')
        response_format = 'json'
        if is_authenticated:
            self.client.force_authenticate(user=self.user)
        for item_number in range(item_numbers):
            data = {'product_id': self.products[item_number].id}
            last_response = self.client.post(url, data=data, format=response_format)
            if item_number + 1 == item_numbers:
                return last_response
        return None

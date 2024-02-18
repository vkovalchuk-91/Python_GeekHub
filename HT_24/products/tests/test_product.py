from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from products.models import Product
from products.tests.factories import ProductFactory, UserFactory


class ProductTestCase(APITestCase):
    client = APIClient()
    maxDiff = None

    def setUp(self):
        self.products = ProductFactory.create_batch(7)
        self.super_user = UserFactory(is_superuser=True)

    def test_create_products(self):
        url = reverse('api_products:product-list')
        data = {'product_ids': '12345'}
        response_format = 'json'
        response = self.client.post(url, data=data, format=response_format)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised

        self.client.force_authenticate(user=self.super_user)
        response = self.client.post(url, data=data, format=response_format)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.content)  # Authorised
        self.assertEqual(response.data['success_message'],
                         'Data has been successfully added to the processing queue!')

    def test_retrieve_product_list(self):
        response = self.client.get(reverse('api_products:product-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)
        self.assertEqual(len(response.data), Product.objects.count())

    def test_retrieve_product_detail(self):
        url = reverse('api_products:product-detail', kwargs={'pk': self.products[4].id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)
        self.assertEqual(response.data['id'], self.products[4].id, msg=response.content)

    def test_delete_product_detail(self):
        start_product_number = Product.objects.count()
        url = reverse('api_products:product-detail', kwargs={'pk': self.products[4].id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised

        self.client.force_authenticate(user=self.super_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.content)  # Authorised
        self.assertEqual(start_product_number, Product.objects.count() + 1)

    def test_patch_product_detail(self):
        url = reverse('api_products:product-detail', kwargs={'pk': self.products[4].id})
        data = {'price': '98.76'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised

        self.client.force_authenticate(user=self.super_user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)  # Authorised
        self.assertEqual(response.data['price'], '98.76')

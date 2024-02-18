from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from products.models import Category
from products.tests.factories import UserFactory, CategoryFactory


class CategoryTestCase(APITestCase):
    client = APIClient()
    maxDiff = None

    def setUp(self):
        self.categories = CategoryFactory.create_batch(3)
        self.super_user = UserFactory(is_superuser=True)

    def test_create_category(self):
        url = reverse('api_products:category-list')
        data = {'name': 'new_category'}
        response_format = 'json'
        response = self.client.post(url, data=data, format=response_format)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised

        self.client.force_authenticate(user=self.super_user)
        response = self.client.post(url, data=data, format=response_format)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.content)  # Authorised
        self.assertEqual(response.data['name'],
                         'new_category')

    def test_retrieve_category_list(self):
        response = self.client.get(reverse('api_products:category-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)
        self.assertEqual(len(response.data), Category.objects.count())

    def test_retrieve_category_detail(self):
        url = reverse('api_products:category-detail', kwargs={'pk': self.categories[1].id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)
        self.assertEqual(response.data['id'], self.categories[1].id, msg=response.content)

    def test_delete_category_detail(self):
        start_category_number = Category.objects.count()
        url = reverse('api_products:category-detail', kwargs={'pk': self.categories[1].id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised

        self.client.force_authenticate(user=self.super_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.content)  # Authorised
        self.assertEqual(start_category_number, Category.objects.count() + 1)

    def test_patch_category_detail(self):
        url = reverse('api_products:category-detail', kwargs={'pk': self.categories[1].id})
        data = {'name': 'updated_category'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.content)  # Unauthorised

        self.client.force_authenticate(user=self.super_user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)  # Authorised
        self.assertEqual(response.data['name'], 'updated_category')

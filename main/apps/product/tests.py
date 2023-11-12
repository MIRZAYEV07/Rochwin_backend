from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, ProductQuantity

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            'name': 'Test Product',
            'quantity': 10,
            'price': 9.99
        }
        self.product = Product.objects.create(**self.product_data)

    def test_create_product(self):
        response = self.client.post('/products/', self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)  # One product already exists in setUp

    def test_get_product_list(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one product in setUp

    def test_get_product_detail(self):
        response = self.client.get(f'/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product_data['name'])

    def test_update_product(self):
        new_quantity = 5
        response = self.client.patch(f'/products/{self.product.id}/', {'quantity': new_quantity}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity, new_quantity)

    def test_update_product_creates_quantity_instance(self):
        new_quantity = 7
        response = self.client.patch(f'/products/{self.product.id}/', {'quantity': new_quantity}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(ProductQuantity.objects.filter(product=self.product).exists())

    def test_update_product_updates_quantity_instance(self):
        existing_quantity = 15
        ProductQuantity.objects.create(product=self.product, quantity=existing_quantity)

        new_quantity = 8
        response = self.client.patch(f'/products/{self.product.id}/', {'quantity': new_quantity}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_quantity = ProductQuantity.objects.get(product=self.product)
        self.assertEqual(product_quantity.quantity, existing_quantity + new_quantity)


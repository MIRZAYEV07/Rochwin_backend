from django.test import TestCase
from rest_framework.test import APIClient
from ...employee.models import Employee


class OrderViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee = Employee.objects.create(full_name='Test Employee', birthdate='1990-01-01')

    def test_create_order(self):
        response = self.client.post('/order/', data={'employee': self.employee.id, 'price': 19.99, 'date': '2023-01-01'})
        self.assertEqual(response.status_code, 201)


    def test_get_order_list(self):
        response = self.client.get('/order-create/')
        self.assertEqual(response.status_code, 200)


    def test_get_order_detail(self):
        response = self.client.get('/order/1/')
        self.assertEqual(response.status_code, 200)


    def test_update_order(self):
        response = self.client.patch('/order-update/1/', data={'price': 29.99}, format='json')
        self.assertEqual(response.status_code, 200)


    def test_get_employee_statistics(self):
        response = self.client.get('/employee-statistic/1/?month=1&year=2023/')
        self.assertEqual(response.status_code, 200)


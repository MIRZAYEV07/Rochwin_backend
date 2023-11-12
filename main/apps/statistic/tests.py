from django.test import TestCase
from rest_framework.test import APIClient

from ..employee.models import Employee
from ..client.models import Client
from ..product.models import Product
from ..order.models import Order
from .serializers import EmployeeStatisticsSerializer, ClientStatisticsSerializer





class EmployeeStatisticsSerializerTestCase(TestCase):
    def test_employee_statistics_serializer(self):
        data = {
            'employee_id': 1,
            'full_name': 'Test Employee',
            'number_of_clients': 5,
            'number_of_products': 20,
            'sales_amount': 199.99,
        }
        serializer = EmployeeStatisticsSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        self.assertEqual(serializer.data['employee_id'], 1)

class ClientStatisticsSerializerTestCase(TestCase):
    def test_client_statistics_serializer(self):
        data = {
            'client_id': 1,
            'full_name': 'Test Client',
            'number_of_purchased_goods': 10,
            'sales_amount': 99.99,
        }
        serializer = ClientStatisticsSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        self.assertEqual(serializer.data['client_id'], 1)


class StatisticsViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee = Employee.objects.create(full_name='Test Employee', birthdate='1990-01-01')
        self.client = Client.objects.create(full_name='Test Client', birthdate='2000-01-01')

    def test_employee_statistics_view(self):
        response = self.client.get('/statistics/employee/1/?month=1&year=2023/')
        self.assertEqual(response.status_code, 200)

    def test_all_employee_statistics_view(self):
        response = self.client.get('/statistics/employees/?month=1&year=2023/')
        self.assertEqual(response.status_code, 200)

    def test_client_statistics_view(self):
        response = self.client.get('/statistics/client/1/?month=1&year=2023/')
        self.assertEqual(response.status_code, 200)




class StatisticsFunctionalityTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee = Employee.objects.create(full_name='Test Employee', birthdate='1990-01-01')
        self.client = Client.objects.create(full_name='Test Client', birthdate='2000-01-01')
        self.product = Product.objects.create(name='Test Product', quantity=10, price=9.99)

    def test_employee_statistics_functionality(self):
        Order.objects.create(client=self.client, employee=self.employee, price=19.99, date='2023-01-01', products=[self.product])
        response = self.client.get('/statistics/employee/1/?month=1&year=2023/')
        self.assertEqual(response.status_code, 200)

    def test_all_employee_statistics_functionality(self):
        Order.objects.create(client=self.client, employee=self.employee, price=19.99, date='2023-01-01', products=[self.product])
        response = self.client.get('/statistics/employees/?month=1&year=2023/')
        self.assertEqual(response.status_code, 200)

    def test_client_statistics_functionality(self):
        Order.objects.create(client=self.client, employee=self.employee, price=19.99, date='2023-01-01', products=[self.product])
        response = self.client.get('/statistics/client/1/?month=1&year=2023/')
        self.assertEqual(response.status_code, 200)

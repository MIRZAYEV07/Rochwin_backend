from django.test import TestCase
from ..serializers import OrderSerializer, EmployeeStatisticsSerializer

from ...employee.models import Employee
from ...client.models import Client
from ...product.models import Product

class OrderSerializerTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(full_name='Test Client', birthdate='2000-01-01')
        self.employee = Employee.objects.create(full_name='Test Employee', birthdate='1990-01-01')
        self.product = Product.objects.create(name='Test Product', quantity=10, price=9.99)

    def test_order_serializer(self):
        data = {
            'client': self.client.id,
            'employee': self.employee.id,
            'products': [self.product.id],
            'price': 19.99,
            'date': '2023-01-01',
        }
        serializer = OrderSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        order_instance = serializer.save()

        self.assertEqual(order_instance.client, self.client)
        self.assertEqual(order_instance.employee, self.employee)


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


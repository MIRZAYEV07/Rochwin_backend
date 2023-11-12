from django.test import TestCase
from ..models import Order
from ...employee.models import Employee
from ...client.models import Client
from ...product.models import Product

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(full_name='Test Client', birthdate='2000-01-01')
        self.employee = Employee.objects.create(full_name='Test Employee', birthdate='1990-01-01')
        self.product = Product.objects.create(name='Test Product', quantity=10, price=9.99)

    def test_calculate_employee_statistics(self):
        Order.objects.create(client=self.client, employee=self.employee, price=19.99, date='2023-01-01', products=[self.product])


        statistics = Order.calculate_employee_statistics(self.employee, month=1, year=2023)

        self.assertEqual(statistics['number_of_clients'], 1)
        self.assertEqual(statistics['number_of_products'], 10)  # Assuming 1 product per order
        self.assertEqual(statistics['sales_amount'], 19.99)  # Total sales amount for the test order

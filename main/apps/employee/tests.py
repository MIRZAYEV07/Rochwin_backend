from django.test import TestCase
from rest_framework.test import APIClient

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeModelTestCase(TestCase):
    def test_create_employee(self):
        employee = Employee.objects.create(full_name='John Doe', birthdate='1990-01-01')
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(employee.full_name, 'John Doe')




class EmployeeSerializerTestCase(TestCase):
    def test_employee_serializer(self):
        data = {'full_name': 'Jane Doe', 'birthdate': '1995-02-15'}
        serializer = EmployeeSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        employee_instance = serializer.save()
        self.assertEqual(employee_instance.full_name, 'Jane Doe')




class EmployeeViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee = Employee.objects.create(full_name='Test Employee', birthdate='1990-01-01')

    def test_create_employee_view(self):
        response = self.client.post('/employee-create/', data={'full_name': 'New Employee', 'birthdate': '1995-05-20'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Employee.objects.count(), 2)


    def test_list_employee_view(self):
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Assuming one employee in the database


    def test_detail_employee_view(self):
        response = self.client.get(f'/employee/{self.employee.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['full_name'], 'Test Employee')


    def test_update_employee_view(self):
        response = self.client.put(f'/employee-update/{self.employee.id}/', data={'full_name': 'Updated Employee', 'birthdate': '1990-01-01'})
        self.assertEqual(response.status_code, 200)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.full_name, 'Updated Employee')





class EmployeeFunctionalityTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee = Employee.objects.create(full_name='Test Employee', birthdate='1990-01-01')

    def test_employee_functionality(self):

        response = self.client.post('/employee-create/', data={'full_name': 'New Employee', 'birthdate': '1995-05-20'})
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Assuming two employees in the database now

        response = self.client.get(f'/employee/{self.employee.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['full_name'], 'Test Employee')

        response = self.client.put(f'/employee-update/{self.employee.id}/', data={'full_name': 'Updated Employee', 'birthdate': '1990-01-01'})
        self.assertEqual(response.status_code, 200)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.full_name, 'Updated Employee')


from django.test import TestCase
from rest_framework.test import APIClient

from .models import Client
from .serializers import ClientSerializer





class ClientModelTestCase(TestCase):
    def test_create_client(self):
        client = Client.objects.create(full_name='John Doe', birthdate='1990-01-01')
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(client.full_name, 'John Doe')



class ClientSerializerTestCase(TestCase):
    def test_client_serializer(self):
        data = {'full_name': 'Jane Doe', 'birthdate': '1995-02-15'}
        serializer = ClientSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        client_instance = serializer.save()
        self.assertEqual(client_instance.full_name, 'Jane Doe')



class ClientViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client_instance = Client.objects.create(full_name='Test Client', birthdate='1990-01-01')

    def test_create_client_view(self):
        response = self.client.post('/clients-create/', data={'full_name': 'New Client', 'birthdate': '1995-05-20'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Client.objects.count(), 2)

    def test_list_client_view(self):
        response = self.client.get('/clients/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Assuming one client in the database

    def test_detail_client_view(self):
        response = self.client.get(f'/client/{self.client_instance.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['full_name'], 'Test Client')

    def test_update_client_view(self):
        response = self.client.put(f'/client-update/{self.client_instance.id}/', data={'full_name': 'Updated Client', 'birthdate': '1990-01-01'})
        self.assertEqual(response.status_code, 200)
        self.client_instance.refresh_from_db()
        self.assertEqual(self.client_instance.full_name, 'Updated Client')




class ClientFunctionalityTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client_instance = Client.objects.create(full_name='Test Client', birthdate='1990-01-01')

    def test_client_functionality(self):

        response = self.client.post('/clients-create/', data={'full_name': 'New Client', 'birthdate': '1995-05-20'})
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/clients/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Assuming two clients in the database now

        response = self.client.get(f'/client/{self.client_instance.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['full_name'], 'Test Client')

        response = self.client.put(f'/client-update/{self.client_instance.id}/', data={'full_name': 'Updated Client', 'birthdate': '1990-01-01'})
        self.assertEqual(response.status_code, 200)
        self.client_instance.refresh_from_db()
        self.assertEqual(self.client_instance.full_name, 'Updated Client')

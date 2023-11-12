from django.db.models.functions import Coalesce
from rest_framework import generics
from django.db.models import Count, Sum
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from ..client.models import Client
from ..employee.models import Employee
from ..order.models import Order
from .serializers import EmployeeStatisticsSerializer, ClientStatisticsSerializer

class EmployeeStatisticsView(generics.RetrieveAPIView):
    serializer_class = EmployeeStatisticsSerializer

    def get_object(self):
        employee_id = self.kwargs.get('id')
        month = self.request.GET.get('month')
        year = self.request.GET.get('year')

        employee = generics.get_object_or_404(Employee, pk=employee_id)
        statistics = self.calculate_employee_statistics(employee, month, year)
        return statistics

    def calculate_employee_statistics(self, employee, month, year):
        orders = Order.objects.filter(employee=employee, date__month=month, date__year=year)

        number_of_clients = orders.values('client').distinct().count()
        number_of_products = orders.aggregate(Sum('products__quantity'))['products__quantity__sum'] or 0
        sales_amount = orders.aggregate(Sum('price'))['price__sum'] or 0

        return {
            'employee_id': employee.id,
            'full_name': employee.full_name,
            'number_of_clients': number_of_clients,
            'number_of_products': number_of_products,
            'sales_amount': sales_amount
        }

class AllEmployeeStatisticsView(generics.ListAPIView):
    serializer_class = EmployeeStatisticsSerializer
    queryset = Employee.objects.all()
    pagination_class = PageNumberPagination



    def list(self, request, *args, **kwargs):
        month = self.request.GET.get('month')
        year = self.request.GET.get('year')
        queryset = Employee.objects.annotate(
            total_products_sold=Coalesce(Sum('order__products__quantity'), 0)
        ).order_by('-total_products_sold')
        statistics = [self.calculate_employee_statistics(employee, month, year) for employee in queryset]
        print(statistics)
        serializer = self.get_serializer(statistics, many=True)
        return Response(serializer.data)

    def calculate_employee_statistics(self, employee, month, year):
        orders = Order.objects.filter(employee=employee, date__month=month, date__year=year)

        number_of_clients = orders.values('client').distinct().count()
        number_of_products = orders.aggregate(Sum('products__quantity'))['products__quantity__sum'] or 0
        sales_amount = orders.aggregate(Sum('price'))['price__sum'] or 0

        return {
            'employee_id': employee.id,
            'full_name': employee.full_name,
            'number_of_clients': number_of_clients,
            'number_of_products': number_of_products,
            'sales_amount': sales_amount
        }

class ClientStatisticsView(generics.RetrieveAPIView):
    serializer_class = ClientStatisticsSerializer

    def get_object(self):
        client_id = self.kwargs.get('id')
        month = self.request.GET.get('month')
        year = self.request.GET.get('year')

        client = generics.get_object_or_404(Client, pk=client_id)
        statistics = self.calculate_client_statistics(client, month, year)
        return statistics

    def calculate_client_statistics(self, client, month, year):
        orders = Order.objects.filter(client=client, date__month=month, date__year=year)

        number_of_purchased_goods = orders.aggregate(Sum('products__quantity'))['products__quantity__sum'] or 0
        sales_amount = orders.aggregate(Sum('price'))['price__sum'] or 0

        return {
            'client_id': client.id,
            'full_name': client.full_name,
            'number_of_purchased_goods': number_of_purchased_goods,
            'sales_amount': sales_amount
        }

from rest_framework import generics

from ..employee.models import Employee
from .models import Order
from .serializers import OrderSerializer, EmployeeStatisticsSerializer


class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'

class EmployeeStatisticsView(generics.RetrieveAPIView):
    serializer_class = EmployeeStatisticsSerializer

    def get_object(self):
        employee_id = self.kwargs.get('id')
        month = self.request.GET.get('month')
        year = self.request.GET.get('year')

        orders = Order.objects.filter(employee=Employee.objects.get(pk=employee_id), date__month=month, date__year=year)

        print(orders,employee_id,month,year)

        employee = Employee.objects.get(pk=employee_id)
        statistics = Order.calculate_employee_statistics(employee, month, year)
        return statistics



# class AllEmployeeStatisticsView(generics.ListAPIView):
#     serializer_class = EmployeeSerializer
#
#     def get_queryset(self):
#         month = self.request.GET.get('month')
#         year = self.request.GET.get('year')
#
#         employees = Order.objects.all()
#         statistics = [employee.calculate_employee_statistics(month, year) for employee in employees]
#         return statistics

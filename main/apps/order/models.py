from django.db import models
from django.db.models import Sum

from ..client.models import Client
from ..employee.models import Employee
from ..product.models import Product


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    @classmethod
    def calculate_employee_statistics(cls, employee, month, year):
        orders = cls.objects.filter(employee=employee, date__month=month, date__year=year)

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




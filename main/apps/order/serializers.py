from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class EmployeeStatisticsSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    full_name = serializers.CharField()
    number_of_clients = serializers.IntegerField()
    number_of_products = serializers.IntegerField()
    sales_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
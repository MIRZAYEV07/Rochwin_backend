from rest_framework import serializers

class EmployeeStatisticsSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    full_name = serializers.CharField()
    number_of_clients = serializers.IntegerField()
    number_of_products = serializers.IntegerField()
    sales_amount = serializers.DecimalField(max_digits=10, decimal_places=2)




class  ClientStatisticsSerializer(serializers.Serializer):
    client_id = serializers.IntegerField()
    full_name = serializers.CharField()
    number_of_purchased_goods = serializers.IntegerField()
    sales_amount = serializers.DecimalField(max_digits=10, decimal_places=2)


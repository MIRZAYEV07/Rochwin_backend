from rest_framework import serializers
from .models import Product, ProductQuantity



class ProductQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuantity
        fields = ['quantity']

class ProductSerializer(serializers.ModelSerializer):
    quantities = ProductQuantitySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'quantities']

    def create(self, validated_data):
        quantities_data = validated_data.pop('quantities', None)
        product = Product.objects.create(**validated_data)


        if quantities_data is None:
            ProductQuantity.objects.create(product=product, quantity=validated_data['quantity'] )
        return product





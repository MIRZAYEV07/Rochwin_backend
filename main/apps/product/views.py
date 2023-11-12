from rest_framework import generics
from rest_framework.response import Response

from .models import Product, ProductQuantity
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()


        try:
            product_quantity = ProductQuantity.objects.get(product=instance)
            product_quantity.quantity += instance.quantity
            product_quantity.save()
        except ProductQuantity.DoesNotExist:
            ProductQuantity.objects.create(product=instance, quantity=instance.quantity)

        return Response(serializer.data)



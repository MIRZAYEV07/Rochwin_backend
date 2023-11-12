from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2
                                )

    def __str__(self):

        return self.name




class ProductQuantity(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='quantities'
    )
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.quantity
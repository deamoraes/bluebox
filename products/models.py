from django.db import models

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    code = models.CharField(max_length=50)
    seller = models.ForeignKey(Seller,null=False,on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()

    STATUS_PRODUCTS = (
        ('A','active'),
        ('I','inactive'),
    )
    product_status = models.CharField(max_length=1,choices=STATUS_PRODUCTS)

    def __str__(self):
        return f"{self.title} - {self.code}"




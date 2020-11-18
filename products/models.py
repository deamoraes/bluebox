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
    seller = models.ForeignKey(Seller,null=False,on_delete=models.SET_DEFAULT)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.code}"




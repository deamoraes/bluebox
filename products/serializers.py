from rest_framework import serializers
from .models import Seller, Product 

class SellerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ["id", "name", "url"]

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price", "code", "seller", "stock_quantity", "url"]
        

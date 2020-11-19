from rest_framework import serializers
from .models import Seller, Product 

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ["id", "name", "url"]

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price", "code", "seller", "stock_quantity", "product_status", "url"]
        

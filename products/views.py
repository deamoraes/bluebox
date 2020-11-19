from django.shortcuts import render
from .models import Seller,Product
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import SellerSerializer,ProductSerializer
import json

class SellerViewSet(generics.ListCreateAPIView):
    queryset = Seller.objects.all().order_by("name")
    serializer_class = SellerSerializer

class SellerDetailViewSet(generics.RetrieveUpdateAPIView):
    queryset = Seller.objects.all().order_by("name")
    serializer_class = SellerSerializer

class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by("title")
    serializer_class = ProductSerializer

class ProductDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by("title")
    serializer_class = ProductSerializer

    def delete(self, request, pk):
        product = self.get_object()
        product.product_status = "I"
        product.save()
        return Response(status=status.HTTP_200_OK)

from django.test import TestCase
from .models import Seller,Product
from rest_framework.test import APIClient
import json

# Unit tests
class SellerModelTest(TestCase):
    def test_class_str(self):
        seller = Seller()
        seller.name = "Samsung"
        self.assertEquals(seller.__str__(), "Samsung")

class ProductModelTest(TestCase):
    def test_class_str(self):
        product = Product()
        seller = Seller()
        seller.name = "Samsung"
        product.title = "Rádio FM"
        product.price = 499.99
        product.code = "aaf4a3r3"
        product.seller = seller
        product.stock_quantity = 60 
        product.product_status = "A"
        self.assertEquals(product.__str__(), "Rádio FM - aaf4a3r3")
         
# API Test cases
class SellerViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Seller.objects.create(name="LG")

    def test_get(self):
        client = APIClient()
        response = client.get('/products/sellers/')

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        self.assertEqual(data.get('count'), 1)

        sellers1 = data.get('results')[0]

        self.assertEqual(sellers1.get("name"), "LG")
      
    def test_post(self):
        client = APIClient()
        response = client.post('/products/sellers/', {
            "name": "Whirpool",
        })

        self.assertEqual(response.status_code, 201)
        self.assertEquals(Seller.objects.count(), 2)
        self.assertEquals(Seller.objects.last().name, "Whirpool")

    def test_put(self):
        client = APIClient()
        response = client.put('/products/sellers/1/', {
            "name": "Sony",
        })

        self.assertEqual(response.status_code, 200)
        self.assertEquals(Seller.objects.count(), 1)
        self.assertEquals(Seller.objects.last().name, "Sony")


 
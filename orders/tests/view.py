from django.test import Client, TestCase
from orders.models import Order, Product
import random

class TestAppViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_pending_view(self):
        response = self.client.get('/new/')
        self.assertEqual(response.status_code, 200)

    def test_preparing_view(self):
        response = self.client.get('/preparing/')
        self.assertEqual(response.status_code, 200)
    
    def test_delivered_view(self):
        response = self.client.get('/completed/')
        self.assertEqual(response.status_code, 200)
    
    def test_sungle_view(self):
        product = Product.objects.create(
            name='Product 1',
            price=10.00
        )

        order = Order.objects.create(
            product=product,
            delivery_address='Address 1',
            quantity=1
        )

        print(order.id)
        response = self.client.get('/single/1/')
        self.assertEqual(response.status_code, 200)


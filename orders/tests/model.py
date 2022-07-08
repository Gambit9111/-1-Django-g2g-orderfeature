from django.test import TestCase

from orders.models import Order, Product


class TestAppModels(TestCase):

    @classmethod
    def setUpTestData(self):
        self.product = Product.objects.create(
            name='Product 1',
            price=10.00
        )

        self.order = Order.objects.create(
            product=self.product,
            delivery_address='Address 1',
            quantity=1
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Product 1 - 10.0')

    def test_order_str(self):
        self.assertEqual(str(self.order), 'Product 1 - 1 - new')

    def test_order_get_total_price(self):
        self.assertEqual(self.order.get_total_price(), 10.00)
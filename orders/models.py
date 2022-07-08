from django.db import models

# product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name + ' - ' + str(self.price)

# order model
class Order(models.Model):

    # order status choices
    STATUS_CHOICES = (
        ('new', 'New'),
        ('preparing', 'Preparing'),
        ('completed', 'Completed'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', 'quantity')

    def __str__(self):
        return self.product.name + ' - ' + str(self.quantity) + ' - ' + self.status

    # function that calculates order price
    def get_total_price(self):
        return self.product.price * self.quantity

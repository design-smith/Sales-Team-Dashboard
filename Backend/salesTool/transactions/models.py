from django.db import models
from products.models import Product
from user_sales.models import SalesUser
from user_customers.models import User

class Transaction(models.Model):
    transaction_date = models.DateTimeField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    products = models.ManyToManyField(Product, related_name='transactions')
    seller = models.ForeignKey(SalesUser, on_delete=models.CASCADE, related_name='transactions')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Perfect for monetary amounts

    def __str__(self):
        return f"Transaction {self.id} on {self.transaction_date}"
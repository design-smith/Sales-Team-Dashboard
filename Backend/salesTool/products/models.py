from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    sku_number = models.CharField(max_length=100, unique=True)  # SKU should be unique
    description = models.TextField()  # TextFields are better for longer descriptions
    date_created = models.DateTimeField(auto_now_add=True)  # Automatically set date when object is created
    last_modified = models.DateTimeField(auto_now=True)  # Automatically set date on save
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for monetary values
    units_sold = models.IntegerField(default=0)  # Use IntegerField for numeric values, default to 0

    def __str__(self):
        return f"{self.name} - SKU: {self.sku_number}"

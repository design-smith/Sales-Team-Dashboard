from django.db import models

class SalesUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    address1 = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)  # Renamed for clarity
    number_of_sales = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Admin: {self.is_admin}"

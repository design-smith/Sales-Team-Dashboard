from rest_framework import serializers
from .models import SalesUser

class SalesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesUser
        fields = ['first_name', 'last_name', 'email', 'contact_number', 'address1', 'is_admin', 'number_of_sales']

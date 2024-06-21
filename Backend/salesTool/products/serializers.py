from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # If you want to explicitly specify the fields to serialize, you can list them as follows:
        # fields = ['name', 'sku_number', 'description', 'date_created', 'last_modified', 'price', 'units_sold']

class ProductSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'units_sold']

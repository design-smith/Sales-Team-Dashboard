from rest_framework import serializers
from .models import Transaction
from products.serializers import ProductSerializer  # Assuming you have a serializer for Product
from user_customers.serializers import UserSerializer  # Assuming you have a serializer for User
from user_sales.serializers import SalesUserSerializer  # Assuming you have a serializer for SalesUser

class TransactionSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    seller = SalesUserSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = [
            'id', 'transaction_date', 'customer', 'products', 'seller'
        ]

    def create(self, validated_data):
        products_data = self.context['request'].data.get('products')
        transaction = Transaction.objects.create(**validated_data)
        transaction.products.set(products_data)
        return transaction

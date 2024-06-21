from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # This includes all fields of the User model in the serializer.

        # Optionally, you can specify fields explicitly if you don't want to include all:
        # fields = ['first_name', 'last_name', 'email', 'contact_number', 'address1', 'address2']

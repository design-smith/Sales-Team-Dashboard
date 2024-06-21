from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .serializers import ProductSalesSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSalesView(APIView):
    def get(self, request):
        # Fetch products with non-zero units sold to display in the chart
        products = Product.objects.filter(units_sold__gt=0)
        serializer = ProductSalesSerializer(products, many=True)
        return Response(serializer.data)
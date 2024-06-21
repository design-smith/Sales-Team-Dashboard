from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, ProductSalesView

# Create a router and register your viewsets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('get_product_sales/', ProductSalesView.as_view(), name='get_product_sales'),
]

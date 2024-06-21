from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import TransactionViewSet

router = DefaultRouter()
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

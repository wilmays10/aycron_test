from django.urls import path, include
from rest_framework import routers
from warehouse.api.views import WarehouseViewSet

router = routers.DefaultRouter()
router.register('warehouses', WarehouseViewSet, basename='warehouse.api.warehouses')


urlpatterns = [
    path('', include(router.urls)),
]

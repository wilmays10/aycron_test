from rest_framework import viewsets
# from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from warehouse.models import Warehouse
from warehouse.api.serializers import WarehouseSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    serializer_class = WarehouseSerializer
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Warehouse.objects.all()

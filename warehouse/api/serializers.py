from rest_framework import serializers

from warehouse.models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = ['code', 'name', 'address']
        depth = 1

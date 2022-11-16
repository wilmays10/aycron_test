from django.contrib import admin
from warehouse.models import Warehouse, Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Address._meta.fields]
    search_fields = ['street', 'zipcode']
    list_filter = ['state', 'county']

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Warehouse._meta.fields]
    search_fields = ['code', 'name', 'address__street', 'address__zipcode']
    list_filter = ['address__state', 'address__county']

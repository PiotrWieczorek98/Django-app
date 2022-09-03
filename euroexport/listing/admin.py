from django.contrib import admin
from .models import Product, OrderEntry, Order, Fabric

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'orderType', 'number', 'received', 'informedProducer', 'status'***REMOVED***


@admin.register(OrderEntry)
class OrderEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'route', 'orderId', 'productId', 'fabricId', 'amount', 'status'***REMOVED***

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'family', 'name', 'price'***REMOVED***

@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'group'***REMOVED***
    list_filter = ['group', 'name'***REMOVED***
    search_fields = ['group', 'name'***REMOVED***
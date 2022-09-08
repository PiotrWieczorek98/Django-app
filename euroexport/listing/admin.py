from django.contrib import admin
from .models import Product, OrderEntry, Order, Fabric

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'orderType', 'number', 'received', 'informedProducer', 'status']


@admin.register(OrderEntry)
class OrderEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'route', 'orderId', 'productId', 'fabricId', 'amount', 'status']
    list_filter = ['route', 'status']
    search_fields = ['productId', 'route']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'family', 'name', 'price', 'ean']
    list_filter = ['family', 'name']
    search_fields = ['family', 'name']

@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'group']
    list_filter = ['group', 'name']
    search_fields = ['group', 'name']
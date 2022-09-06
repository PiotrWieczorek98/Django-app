from django.contrib.auth.models import User, Group
from .models import Order, Product, Fabric, OrderEntry
from rest_framework import  serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups'***REMOVED***

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name'***REMOVED***

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['shop', 'orderType', 'number', 'received', 'informedProducer', 'status'***REMOVED***
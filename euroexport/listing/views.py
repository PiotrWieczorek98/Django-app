from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Order
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, GroupSerializer, OrderSerializer

# API endpoints that allows users to be viewed or edited.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated***REMOVED***
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        self.perform_create(serializer)
        data = serializer.data
        headers = self.get_success_headers(data)
        data['token'***REMOVED*** = Token.objects.get(user=account).key
        return Response(data, headers=headers)

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated***REMOVED***
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated***REMOVED***
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
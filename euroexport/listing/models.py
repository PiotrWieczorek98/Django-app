from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models import signals
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.
class Account(User):
    class Meta:
        proxy = True

    @receiver(signals.post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

class Order(models.Model):
    Shops =[('tp', 'Tempo Kondela'),('ps', 'Posed')]
    OrderType = [('cs', 'Customer'), ('st', 'Storage'), ('cp', 'Complaint')]
    Status = [('pd', 'Pending'), ('ct', 'Complited')]

    shop = models.CharField(choices=Shops, max_length=20)
    orderType = models.CharField(choices=OrderType, default='cs', max_length=20)
    number = models.CharField(max_length=50, unique=True)
    received = models.DateField()
    informedProducer = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=Status, default='pd')

    def __str__(self):
        return f'{self.shop} {self.number} {self.received}'

class Product(models.Model):
    ConfigurationType = [(False, 'Regular'), (True, 'Custom')]

    family = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    configurationType = models.BooleanField(choices=ConfigurationType, default=False)
    configuration = models.CharField(max_length=50)
    ean = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f'{self.family} {self.name}'

class Fabric(models.Model):
    Groups = [('1', 'First'), ('2', 'Second'), ('3', 'Third')]

    name = models.CharField(max_length=50)
    number = models.SmallIntegerField()
    group = models.CharField(choices=Groups, default='1', max_length=10)

    def __str__(self):
        return f'{self.name} {self.number} {self.group}'

class OrderEntry(models.Model):
    Status = [('st', 'Sent'), ('ip', 'In production'), ('cc', 'Canceled'), ('rt', 'Returned')]

    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    productId = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, blank=True)
    fabricId = models.ForeignKey(Fabric, on_delete=models.DO_NOTHING, null=True, blank=True)

    route = models.CharField(null=True, blank=True, max_length=50)
    customer = models.CharField(null=True, blank=True, max_length=50)
    amount = models.IntegerField(default=1)
    info = models.CharField(null=True, blank=True, max_length=200)
    dispatched = models.DateField(null=True, blank=True)
    status = models.CharField(choices=Status, default='ip', max_length=20)

    def __str__(self):
        return f'Order entry No.{self.id}'
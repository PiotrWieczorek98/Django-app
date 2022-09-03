from django.db import models

# Create your models here.


class Order(models.Model):
    Shops =[('tp', 'Tempo Kondela'),('ps', 'Posed')***REMOVED***
    OrderType = [('cs', 'Customer'), ('st', 'Storage'), ('cp', 'Complaint')***REMOVED***
    Status = [('pd', 'Pending'), ('ct', 'Complited')***REMOVED***

    shop = models.CharField(choices=Shops, max_length=20)
    orderType = models.CharField(choices=OrderType, default='cs', max_length=20)
    number = models.CharField(max_length=50)
    received = models.DateField()
    informedProducer = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=Status, default='pd')

    def __str__(self):
        return f'{self.shop***REMOVED*** {self.number***REMOVED*** {self.received***REMOVED***'

class Product(models.Model):
    ConfigurationType = [(False, 'Regular'), (True, 'Custom')***REMOVED***

    family = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    configurationType = models.BooleanField(choices=ConfigurationType, default=False)
    configuration = models.CharField(max_length=50)
    ean = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.family***REMOVED*** {self.name***REMOVED***'

class Fabric(models.Model):
    Groups = [('1', 'First'), ('2', 'Second'), ('3', 'Third')***REMOVED***

    name = models.CharField(max_length=50)
    number = models.SmallIntegerField()
    group = models.CharField(choices=Groups, default='1', max_length=10)

    def __str__(self):
        return f'{self.name***REMOVED*** {self.number***REMOVED*** {self.group***REMOVED***'

class OrderEntry(models.Model):
    Status = [('st', 'Sent'), ('ip', 'In production'), ('cc', 'Canceled'), ('rt', 'Returned')***REMOVED***

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
        return f'Order entry No.{self.id***REMOVED***'
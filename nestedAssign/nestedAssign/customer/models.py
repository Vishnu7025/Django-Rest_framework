from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    def __str__(self):
        return self.firstName+ ' ' +self.lastName

class Order(models.Model):
    product = models.CharField(max_length=40)
    quantity = models.CharField(max_length=40)
    customer = models.ForeignKey(Customer,related_name='orders',on_delete=models.CASCADE)
  
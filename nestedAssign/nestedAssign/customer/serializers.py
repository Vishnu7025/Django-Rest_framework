from . models import Customer,Order
from rest_framework import serializers

class orderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class customerSerializers(serializers.ModelSerializer):
    orders = orderSerializers(read_only = True,many = True)
    class Meta:
        model = Customer
        fields = '__all__'
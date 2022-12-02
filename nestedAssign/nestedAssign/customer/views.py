from . models import Customer,Order
from . serializers import orderSerializers,customerSerializers
from rest_framework import generics
# Create your views here.

class customerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerSerializers
class customerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerSerializers

class orderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = orderSerializers
class orderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = orderSerializers



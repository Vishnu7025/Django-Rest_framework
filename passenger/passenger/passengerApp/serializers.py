from rest_framework import serializers
from . models import Passenger

class passengerSerilalizers(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id','firstName','lastName','travelPoint']
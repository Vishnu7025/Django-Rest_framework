from rest_framework import serializers
from courseApp.models import Course

class courseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name','desc','rate']
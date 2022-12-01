from rest_framework import serializers
from cbvApp . models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Student
        fields = ['id','name','score']
from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serilaizers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics
# Create your views here.

class student_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class student_detail(mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)


# class student_list(APIView):
#     def get(self,request):
#         student = Student.objects.all()
#         serializer = StudentSerializers(student,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class student_detail(APIView):
#     def get_object(self,pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             raise Http404
#     def get(self,request,pk):
#         student = self.get_object(pk)
#         serializer = StudentSerializers(student)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         student = self.get_object(pk)
#         serializer = StudentSerializers(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         student = self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
from courseApp.models import Course
from courseApp.serializers import courseSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.
class StudentPagination(PageNumberPagination):
    page_size = 1

class course_viewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = courseSerializers
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','id']


# class course_list(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = courseSerializers

# class course_details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = courseSerializers


# class course_list(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Course.objects.all()
#     serializer_class = courseSerializers

#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    
# class course_details(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Course.objects.all()
#     serializer_class = courseSerializers
    
    # def get(self,request,pk):
    #     return self.retrieve(request,pk)
    # def put(self,request,pk):
    #     return self.update(request,pk)
    # def delete(self,request,pk):
    #     return self.destroy(request,pk)


# class course_list(APIView):
#     def get(self,request):
#         course = Course.objects.all()
#         serializer = courseSerializers(course,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = courseSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class course_detail(APIView):
#     def get_object(self,pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404
#     def get(self,request,pk):
#         course =  self.get_object(pk)
#         serializer = courseSerializers(course)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         course = self.get_object(pk)
#         serializer = courseSerializers(course,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         course = self.get_object(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
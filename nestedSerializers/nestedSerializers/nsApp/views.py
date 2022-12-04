from nsApp.serializers import BookSerializer,AuthorSerializer
from rest_framework import generics
from nsApp.models import Author,Book
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class list_author(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
class deatis_author(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class list_book(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class detail_book(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
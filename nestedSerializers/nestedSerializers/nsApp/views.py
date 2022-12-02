from nsApp.serializers import BookSerializer,AuthorSerializer
from rest_framework import generics
from nsApp.models import Author,Book
# Create your views here.
class list_author(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
class deatis_author(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class list_book(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class detail_book(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
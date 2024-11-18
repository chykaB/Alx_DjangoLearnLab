from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics, viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
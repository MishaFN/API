from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics
from bookapp.models import Books


class BookApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class UniversalApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
class CreateApiView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


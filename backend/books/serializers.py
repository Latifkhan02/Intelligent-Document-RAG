from rest_framework import serializers
from .models import Book

# Here we have a nested Meta class inside the main one 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

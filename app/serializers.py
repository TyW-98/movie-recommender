from rest_framework import serializers
from .models import Book, BookUniqueNumber

class BookUniqueNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookUniqueNumber
        fields = ['id', 'ISBN_10', 'ISBN_13']
        
class BookSerializer(serializers.ModelSerializer):
    uniqueNumber = BookUniqueNumberSerializer(many=False)

    class Meta: 
        model = Book
        fields = ['id', 'title', 'published_date', 'price', 'stock', 'uniqueNumber']

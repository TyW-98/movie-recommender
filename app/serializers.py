from rest_framework import serializers
from .models import Book, BookUniqueNumber, Character

class BookUniqueNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookUniqueNumber
        fields = ['id', 'ISBN_10', 'ISBN_13']
        
class ChracterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Character
        fields = ['id', 'name']
        
class BookSerializer(serializers.ModelSerializer):
    uniqueNumber = BookUniqueNumberSerializer(many=False)
    characters = ChracterSerializer(many=True, read_only=True)

    class Meta: 
        model = Book
        fields = ['id', 'title', 'published_date', 'price', 'stock', 'uniqueNumber', 'characters']
        

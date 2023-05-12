from django.contrib import admin
from .models import Book, BookUniqueNumber, Character, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    # Change what is shown in individual object
    # fields = ['title', 'price', 'stock']
    # Change what is shown in the model's table
    list_display = ['title', 'price', 'stock']
    list_filter = ['published_date', 'price']
    search_fields = ['title']
    
@admin.register(BookUniqueNumber)
class BookUniqueNumberAdmin(admin.ModelAdmin):
    
    list_display = ["ISBN_10", "ISBN_13"]
    
@admin.register(Character)
class CharactersAdmin(admin.ModelAdmin):
    
    list_display = ["name"]
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    
    list_display = ["name"]
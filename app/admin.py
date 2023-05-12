from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    # Change what is shown in individual object
    # fields = ['title', 'price', 'stock']
    # Change what is shown in the model's table
    list_display = ['title', 'price', 'stock']
    list_filter = ['published_date', 'price']
    search_fields = ['title']
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Book

# Create your views here.
class BasicView(View):
    
    books = Book.objects.all()
    # Filter the books
    # books = Book.objects.filter(id__exact=1)
    # Get one object
    # books = Book.objects.get(id = 1)
    
    # def get(self, request):
    #     return HttpResponse(f"There is {len(self.books)} books in the database with books such as {self.books[0].title} and {self.books[1].title}")
    
    def get(self, request):
        return render(request, 'index.html', {'bookList': self.books})

def basic_view(request):
    return HttpResponse('Basic View')
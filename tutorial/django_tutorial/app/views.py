from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Book
from .serializers import BookMiniSerializer, BookSerializer


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
        return render(request, "index.html", {"bookList": self.books})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # Retrieve all details of a single record when querying individual records

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


def basic_view(request):
    return HttpResponse("Basic View")

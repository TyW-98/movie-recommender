from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Actor, CustomUser, Director, Movie, RatedMovies
from .serializers import (
    ActorMiniSerializer,
    ActorSerializer,
    CustomUserMiniSerializer,
    CustomUserSerializer,
    DirectorMiniSerializer,
    DirectorSerializer,
    MovieMiniSerializer,
    MovieSerializer,
    RatedMovieMiniSerializer,
)


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieMiniSerializer
    queryset = Movie.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializer(instance)
        return Response(serializer.data)


class DirectorViewSet(viewsets.ModelViewSet):
    serializer_class = DirectorMiniSerializer
    queryset = Director.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DirectorSerializer(instance)
        return Response(serializer.data)


class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = ActorMiniSerializer
    queryset = Actor.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ActorSerializer(instance)
        return Response(serializer.data)


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserMiniSerializer
    queryset = CustomUser.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CustomUserSerializer(instance)
        return Response(serializer.data)


class RatedMoviesViewSet(viewsets.ModelViewSet):
    serializer_class = RatedMovieMiniSerializer
    queryset = RatedMovies.objects.all()

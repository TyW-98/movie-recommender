from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
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
class BaseModelViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_classes = {
        "movie": MovieSerializer,
        "director": DirectorSerializer,
        "actor": ActorSerializer,
        "customuser": CustomUserSerializer,
        "ratedmovie": RatedMovieMiniSerializer,
    }

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        model_class = instance.__class__.__name__.lower()
        serializer_class = self.serializer_classes.get(
            model_class, self.serializer_class
        )
        serializer = serializer_class(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            response = {"message": "You do not have permission for this method"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            response = {"message": "You do not have permission for this method"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            response = {"message": "You do not have permission for this method"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        return super().create(request, *args, **kwargs)


class MovieViewSet(BaseModelViewSet):
    serializer_class = MovieMiniSerializer
    queryset = Movie.objects.all()

    @action(detail=True, methods=["POST"])
    def rate_movie(self, request, pk=None):
        if "rating" in request.data:
            movie = Movie.objects.get(id=pk)
            rating = request.data["rating"]
            user = request.user

            try:
                user_rating = RatedMovies.objects.get(user=user.id, movie=movie.id)
                user_rating.user_rating = rating
                user_rating.save()
                serializer = RatedMovieMiniSerializer(user_rating)
                response = {
                    "Message": "Movie rating updated",
                    "output": serializer.data,
                }
                return Response(response, status=status.HTTP_200_OK)
            except:
                user_rating = RatedMovies.objects.create(
                    user=user, movie=movie, user_rating=rating
                )
                serailizer = RatedMovieMiniSerializer(user_rating)
                response = {
                    "Message": "Movie rating created",
                    "output": serailizer.data,
                }
                return Response(response, status=status.HTTP_201_CREATED)

        else:
            response = {"Message": "Please include your rating"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class DirectorViewSet(BaseModelViewSet):
    serializer_class = DirectorMiniSerializer
    queryset = Director.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DirectorSerializer(instance)
        return Response(serializer.data)


class ActorViewSet(BaseModelViewSet):
    serializer_class = ActorMiniSerializer
    queryset = Actor.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ActorSerializer(instance)
        return Response(serializer.data)


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserMiniSerializer
    queryset = CustomUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CustomUserSerializer(instance)
        return Response(serializer.data)


class RatedMoviesViewSet(viewsets.ModelViewSet):
    serializer_class = RatedMovieMiniSerializer
    queryset = RatedMovies.objects.all()


# TODO: Add more restrictions

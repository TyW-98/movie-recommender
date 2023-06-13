from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication,
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Actor, CustomUser, Director, Movie, RatedMovies
from .serializers import (
    ActorDetailedSerializer,
    ActorSerializer,
    CustomUserDetailedSerializer,
    CustomUserSerializer,
    DirectorDetailedSerializer,
    DirectorSerializer,
    MovieDetailedSerializer,
    MovieSerializer,
    RatedMovieSerializer,
)

# Create your views here.
class BaseModelViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    
    serializer_class = {
        "movie": MovieDetailedSerializer,
        "director": DirectorDetailedSerializer,
        "actor": ActorDetailedSerializer,
        "ratedmovie": RatedMovieSerializer
    }
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        model_class = instance.__class__.__name__.lower()
        serializer_class = self.serializer_class.get(
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
        
        return super().destroy(request, *args, **kwargs)
    
class MovieViewset(BaseModelViewset):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    
    @action(detail=True, methods=["POST"])
    def rate_movie(self, request, pk=None):
        if "rating" in request.data:
            movie = Movie.object.get(id=pk)
            rating = request.data["rating"]
            user = request.user
            
            try: 
                user_rating = RatedMovies.objects.get(user = user.id, movie=movie.id)
                user_rating.user_rating = rating
                user_rating.save()
                serializer = RatedMovieSerializer(user_rating)
                response = {
                    "Message": "Movie rating updated",
                    "output": serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            except RatedMovies.DoesNotExist:
                user_rating = RatedMovies.objects.create(
                    user=user, movie=movie, user_rating=rating
                )
                serializer = RatedMovieSerializer(user_rating)
                response = {
                    "Message": "Movie rating created",
                    "output": serializer.data
                }
                return Response(response, status=status.HTTP_201_CREATED)
            
        else: 
            response = {
                "Message": "Please include your rating"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
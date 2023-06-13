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
        "ratedmovie": RatedMovieSerializer,
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
        
class DirectorViewset(BaseModelViewset):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()
    
class ActorViewset(BaseModelViewset):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
    
class RatedMoviesViewset(BaseModelViewset):
    serializer_class = RatedMovieSerializer
    queryset = RatedMovies.objects.all()

class CustomUserviewset(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    
    def get_token(self):
        permission_classes = (
            [AllowAny]
            if self.action == "create" or self.action == "user_rated_movies"
            else [IsAdminUser]
        )
        
        return [permission() for permission in permission_classes]
    
    def get_information(self):
        user = self.request.user
        if user.is_authenticated:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=user.id)
    
    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:
            instance = self.get_object()
            serializer = CustomUserDetailedSerializer(instance)
            return Response(serializer)
        
    @action(detail=False, methods=["GET"], permission_classes = [IsAuthenticated,])
    def user_rated_movies(self, request):
        user = request.user.id
        user_data = RatedMovies.objects.filter(user=user)
        serializer = RatedMovieSerializer(user_data, many= True)
        response = {
            "message": "Rated movies for the user",
            "output": serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
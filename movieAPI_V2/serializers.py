from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Actor, CustomUser, Director, Movie, RatedMovies


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            "id",
            "name",
        ]


class ActorDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "name", "movies"]


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["id", "name"]


class DirectorDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["id", "name", "movies"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "MPAA_rating", "language", "poster_image_url"]


class MovieDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "released_year",
            "genre",
            "MPAA_rating",
            "language",
            "duration",
            "director",
            "cast",
            "trailer_url",
            "poster_image_url",
        ]


class RatedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatedMovies
        fields = ["id", "user", "movie", "user_rating"]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "display_name", "email", "dob"]


class CustomUserDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "password",
            "dob",
            "display_name",
            "gender",
            "country",
        ]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validate_data):
        validate_data["password"] = make_password(validate_data["password"])
        user = CustomUser.objects.create(**validate_data)
        Token.objects.create(user=user)
        return user

    def update(self, instance, validate_data):
        instance.set_password(validate_data["password"])
        instance.save()
        return instance

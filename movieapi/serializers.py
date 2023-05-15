from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Actor, CustomUser, Director, Movie, RatedMovies


class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "genre",
            "language",
            "published_date",
            "average_rating",
        ]


class MovieMiniMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title"]


class DirectorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["id", "name"]


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieMiniMiniSerializer(many=True)

    class Meta:
        model = Director
        fields = ["name", "movies"]


class ActorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieMiniMiniSerializer(many=True)

    class Meta:
        model = Actor
        fields = [
            "id",
            "name",
            "movies",
        ]


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorMiniSerializer(many=False)
    actors = ActorMiniSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "genre",
            "language",
            "published_date",
            "metascore",
            "average_rating",
            "duration",
            "director",
            "actors",
        ]


class RatedMovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatedMovies
        fields = ["id", "user", "movie", "user_rating"]


class CustomUserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = CustomUser.objects.create(**validated_data)
        Token.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class CustomUserSerializer(serializers.ModelSerializer):
    ratedmovies = RatedMovieMiniSerializer(many=True)
    country = serializers.CharField(source="country.name")

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "preferred_name",
            "username",
            "email",
            "age",
            "country",
            "ratedmovies",
        ]

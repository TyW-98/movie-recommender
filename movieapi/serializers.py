from rest_framework import serializers

from .models import Actor, CustomUser, Director, Movie, RatedMovies


class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "language", "published_date"]


class DirectorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["id", "name"]


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieMiniSerializer(many=True)

    class Meta:
        model = Director
        fields = ["name", "movies"]


class ActorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieMiniSerializer(many=True)

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
            "duration",
            "director",
            "actors",
        ]


class RatedMovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatedMovies
        fields = ["id", "movie", "userRating"]


class CustomUserMiniSerializer(serializers.ModelSerializer):
    model = CustomUser
    fields = ["id", "username", "country"]


class CustomUserSerializer(serializers.ModelSerializer):
    user_rated_movies = RatedMovieMiniSerializer(many=False)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "preferred_name",
            "username",
            "email",
            "age",
            "country",
            "user_rated_movies",
        ]

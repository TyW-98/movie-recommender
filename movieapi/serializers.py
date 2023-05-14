from rest_framework import serializers

from .models import Actor, CustomUser, Director, Movie, RatedMovies


class MovieMiniSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "language", "published_date"]


class DirectorMiniSerializer(serializers.Serializer):
    class Meta:
        model = Director
        fields = ["id", "name"]


class DirectorSerializer(serializers.Serializer):
    movies = MovieMiniSerializer(many=True)

    class Meta:
        model = Director
        fields = ["id", "name", "movies"]


class ActorMiniSerializer(serializers.Serializer):
    class Meta:
        model = Actor
        fields = ["id", "name"]


class ActorSerializer(serializers.Serializer):
    movies = MovieMiniSerializer(many=True)

    class Meta:
        model = Actor
        fields = [
            "id",
            "name",
            "movies",
        ]


class MovieSerializer(serializers.Serializer):
    director = DirectorMiniSerializer(many=False)
    actor = ActorSerializer(many=True)

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
            "actor",
        ]


class RatedMovieMiniSerializer(serializers.Serializer):
    class Meta:
        model = RatedMovies
        fields = ["id", "movie", "userRating"]


class CustomUserMiniSerializer(serializers.Serializer):
    model = CustomUser
    fields = ["id", "username", "country"]


class CustomUserSerializer(serializers.Serializer):
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

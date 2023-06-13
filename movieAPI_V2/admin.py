from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Actor, CustomUser, Director, Movie, RatedMovies


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ("-last_login",)
    list_display = [
        "id",
        "username",
        "email",
        "date_joined",
        "last_login",
        "is_active",
        "is_staff",
    ]
    search_fields = ("username", "email")
    list_filter = ("country", "gender", "last_login", "is_active", "is_staff")

    fieldsets = (
       (None, {
           "fields": ("email", "username")
       }),
       ("Personal Info", {
           "fields": ("display_name", "gender", "dob", "country")
       }),
       ("Permissions", {
           "fields": ("is_active", "is_staff")
       }),
       ("Important Dates", {
           "fields": ("last_login", "date_joined")
       }),
    )

    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "username",
                "password1",
                "password2",
                "email",
                "dob",
                "gender",
                "country",
            ),
        },
    )


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ("name",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ("name",)


@admin.register(RatedMovies)
class RatedMoviesAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
    search_fields = ("user",)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ordering = ("-released_year",)
    list_display = [
        "id",
        "title",
        "genre",
        "language",
        "released_year",
        "MPAA_rating",
    ]
    search_fields = ("title",)
    list_filter = ("genre", "released_year", "language", "MPAA_rating")
    
    fieldsets = (
        (None, {
            "fields": ("title",)
        }),
        ("Movie Details", {
            "fields": ("released_year", "genre", "language", "MPAA_rating")
        }),
        ("Director / Cast", {
            "fields": ("director", "cast")
        }),
        ("Images / Trailer", {
            "fields": ("trailer_url", "poster_image_url")
        }),
    )
    
    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
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
            ),
        },
    )
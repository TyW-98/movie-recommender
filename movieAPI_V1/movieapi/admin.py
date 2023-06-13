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
        "country",
        "date_joined",
        "last_login",
        "is_active",
        "is_staff",
    ]
    search_fields = ("username", "email")
    list_filter = ("country", "last_login")
    fieldsets = (
        (
            "Details",
            {
                "fields": (
                    "username",
                    "email",
                    "preferred_name",
                    "age",
                    "gender",
                    "country",
                    "date_joined",
                )
            },
        ),
        ("Status", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "age",
                    "gender",
                    "country",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ordering = ("-published_date",)
    list_display = [
        "id",
        "title",
        "genre",
        "language",
        "published_date",
        "average_rating",
        "duration",
    ]
    search_fields = ("title",)
    list_filter = ("genre", "language", "published_date", "metascore")


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "dob"]
    search_fields = ("name",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "dob"]
    search_fields = ("name",)


@admin.register(RatedMovies)
class RatedMoviesAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
    search_fields = ("user",)

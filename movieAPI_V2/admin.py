from django.contrib import admin

from .models import Actor, CustomUser, Director, Movie, RatedMovies

# Register your models here.
admin.site.register(Movie)
admin.site.register(CustomUser)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(RatedMovies)

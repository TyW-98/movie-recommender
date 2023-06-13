from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import (
    ActorViewset,
    CustomUserviewset,
    DirectorViewset,
    MovieViewset,
    RatedMoviesViewset,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewset)
router.register("users", CustomUserviewset)
router.register("ratings", RatedMoviesViewset)


urlpatterns = [path("", include(router.urls))]
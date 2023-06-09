from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .views import (
    ActorViewSet,
    CustomUserViewSet,
    DirectorViewSet,
    MovieViewSet,
    RatedMoviesViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("directors", DirectorViewSet)
router.register("users", CustomUserViewSet)
router.register("ratings", RatedMoviesViewSet)

urlpatterns = [path("", include(router.urls))]

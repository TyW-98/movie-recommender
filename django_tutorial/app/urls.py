from django.urls import path, include
from rest_framework import routers
from . import views
from .views import BookViewSet

router = routers.DefaultRouter()
router.register("books", BookViewSet)

urlpatterns = [
    # path('', views.basic_view),
    path("", views.BasicView.as_view()),
    path("book/", include(router.urls)),
]

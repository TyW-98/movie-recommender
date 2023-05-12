from django.urls import path
from . import views

urlpatterns = [
    # path('', views.basic_view),
    path("",views.BasicView.as_view())
]
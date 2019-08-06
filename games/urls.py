# from django.conf.urls import url
from django.urls import path
from .views import game_collection, game_detail

urlpatterns = [
    path('games/', game_collection),
    path('games/<int:id>/', game_detail),
]

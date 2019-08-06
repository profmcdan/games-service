# from django.conf.urls import url
from django.urls import path
# from .views import game_collection, game_detail
from . import views

urlpatterns = [
    path('esrb-ratings/', views.EsrbRatingList.as_view(),
         name=views.EsrbRatingList.name),
    path('esrb-ratings/<int:pk>/', views.EsrbRatingDetail.as_view(),
         name=views.EsrbRatingDetail.name),
    path('games/', views.GameList, name=views.GameList.name),
    path('games/<int:pk>/', views.GameDetail.as_view(),
         name=views.GameDetail.name),
    path('players/', views.PlayerList.as_view(), name=views.PlayerList.name),
    path('players/<int:pk>/', views.PlayerDetail.as_view(),
         name=views.PlayerDetail.name),
    path('player-scores/', views.PlayerScoreList.as_view(),
         name=views.PlayerScoreList.name),
    path('player-scores/<int:pk>/', views.PlayerScoreDetail.as_view(),
         name=views.PlayerScoreDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

]

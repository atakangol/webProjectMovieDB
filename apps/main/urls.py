from datetime import timezone, datetime
from django.urls import path
from django.views.generic import DetailView, ListView
from .models import Favorite_Movie, Movie
from .views import home, FavoriteMovieCreate, RemoveFavoriteMovie, RemoveFavoriteMovieFromHome

app_name = "movies"

urlpatterns = [
    path('', home, name='url_home'),
    path('addfavorite/<int:pk>', FavoriteMovieCreate, name='url_add_favorite'),
    path('removefavorite/<int:pk>', RemoveFavoriteMovie, name='url_remove_favorite'),
    path('removefavoritefromhome/<int:pk>', RemoveFavoriteMovieFromHome),
    path('details/<int:pk>', DetailView.as_view(model=Movie, template_name='movies/movies_detail.html'), name='url_movie_detail'),
]

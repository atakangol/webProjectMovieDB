from datetime import timezone, datetime
from django.urls import path
from django.views.generic import DetailView, ListView
from .models import Favorite_Movie, Movie
from .views import HomePage, FavoriteMovieCreate, RemoveFavoriteMovie, MovieDetail, EditFavoriteMovie

#app_name = "movies"

urlpatterns = [
    path('', HomePage, name='url_home'),
    path('addfavorite/<int:pk>', FavoriteMovieCreate, name='url_add_favorite'),
    path('editfavorite/<int:pk>', EditFavoriteMovie, name='url_edit_favorite'),
    path('removefavorite/<int:pk>', RemoveFavoriteMovie, name='url_remove_favorite'),
    path('details/<int:pk>', MovieDetail, name='url_movie_detail'),
]

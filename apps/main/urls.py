from datetime import timezone, datetime

from django.urls import path
from django.views.generic import DetailView, ListView

from .models import Favorite_Movie
from .views import home, MovieCreate

app_name = "movies"

urlpatterns = [
    path('', home, name='url_home'),

    # Create a movie
    path('movie/create',
         MovieCreate.as_view(),
         name='movie_create'),

    # Movies details, /movies/1
    path('movies/<int:pk>',
         DetailView.as_view(
             model=Favorite_Movie,
             template_name='movies/movies_detail.html'),
         name='movie_detail'),

    # List latest 4 movies: /mymovies/
    path('profile/',
         ListView.as_view(
             queryset=Favorite_Movie.objects, #.filter(date__lte=datetime.now()).order_by('-date')[:5],
             context_object_name='latest_restaurant_list',
             template_name='movies/movie_list.html'),
         name='movie_list'),
]

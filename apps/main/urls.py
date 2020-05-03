from django.urls import path
from django.views.generic import DetailView

from .models import Movie
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
             model=Movie,
             template_name='movies/movies_detail.html'),
         name='movie_detail'),
]

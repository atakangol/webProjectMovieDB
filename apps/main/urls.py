from django.urls import path
from .views import home, MovieCreate

app_name = "movies"

urlpatterns = [
    path('', home, name='url_home'),

    # Create a movie, /apps/main/
    path('movie/create',
         MovieCreate.as_view(),
         name='movie_create'),
]

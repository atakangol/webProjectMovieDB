from django.urls import path
from django.views.generic.edit import CreateView

from .forms import MovieForm
from .models import Movie
from .views import home


app_name = "main"

urlpatterns = [
    path('', home, name='url_home'),

    # Create a movie, /apps/main/movie/create/
    path('movie/create',
         CreateView.as_view(
             model=Movie,
             template_name='apps/main/form.html',
             form_class=MovieForm),
         name='movie_create',
         )
]

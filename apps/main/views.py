from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from . import models
from .forms import MovieForm
from .models import Movie, Favorite_Movie
from django.contrib.auth import authenticate, login


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'home.html', context)


class MovieCreate(LoginRequiredMixin, CreateView):
    model = Favorite_Movie
    template_name = 'movies/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self).form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .forms import MovieForm
from .models import Movie
from django.contrib.auth import authenticate, login


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'home.html', context)


class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'apps/main/templates/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self).form_valid(form)

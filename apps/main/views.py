from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from . import models
from .forms import FavoriteMovieForm
from .models import Movie, Favorite_Movie
from django.contrib.auth import authenticate, login
from django import forms


def home(request):
    movies = Movie.objects.all()
    favorite_movies = Favorite_Movie.objects.all()
    context = {
        'movies': movies,
        'favorites': favorite_movies 
    }
    return render(request, 'home.html', context)

def FavoriteMovieCreate(request, pk):
    movie_clicked = Movie.objects.get(pk=pk)
    form = FavoriteMovieForm(initial={'movieName': movie_clicked.movieName,
                                    'movieID': movie_clicked.movieID,
                                    'userID': request.user})
    if request.method == 'POST':
        form = FavoriteMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'movies/add_favorite.html', {'form':form, 'movie':movie_clicked}) 


#class FavoriteMovieCreate(LoginRequiredMixin, CreateView):
#    model = Favorite_Movie
#    template_name = 'movies/add_favorite.html'
#    form_class = FavoriteMovieForm
#
#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        return super(FavoriteMovieCreate, self).form_valid(form)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from . import models
from .forms import FavoriteMovieForm
from .models import Movie, Favorite_Movie, Casting
from django.contrib.auth import authenticate, login
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def home(request):
    movies = Movie.objects.all()
    favorite_movies = Favorite_Movie.objects.filter(userID=request.user.id).values_list('movieID', flat=True)
    context = {
        'movies': movies,
        'favorites': favorite_movies 
    }
    return render(request, 'home.html', context)

@login_required
def FavoriteMovieCreate(request, pk):
    movie_clicked = Movie.objects.get(pk=pk)
    form = FavoriteMovieForm(initial={'movieID': movie_clicked,
                                    'userID': request.user})
    form.fields['favActorID'].queryset = Casting.objects.filter(movieID=pk)
    if request.method == 'POST':
        form = FavoriteMovieForm(request.POST)
        movie_exists = Favorite_Movie.objects.filter(movieID=movie_clicked)
        if form.is_valid():
            if movie_exists:
                Favorite_Movie.objects.filter(movieID=movie_clicked).delete()
            form.save()
            return redirect('/')
    context = {
        'form': form,
        'movie': movie_clicked
    }

    return render(request, 'movies/add_favorite.html', context) 

#Remove a movie from favorite movies by profile
def RemoveFavoriteMovie(request, pk):
    movie_clicked = Movie.objects.get(pk=pk)
    movie_instance = Favorite_Movie.objects.filter(movieID=movie_clicked).delete()
    return HttpResponseRedirect('/profile')

#Remove a movie from favorite movies by homepage
def RemoveFavoriteMovieFromHome(request, pk):
    movie_clicked = Movie.objects.get(pk=pk)
    movie_instance = Favorite_Movie.objects.filter(movieID=movie_clicked).delete()
    return HttpResponseRedirect('/')



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


def HomePage(request):
    movies = Movie.objects.all()
    favorite_movies = Favorite_Movie.objects.filter(userID=request.user.id).values_list('movieID', flat=True)
    context = {
        'movies': movies,
        'favorites': favorite_movies
    }
    return render(request, 'home.html', context)

def MovieDetail(request, pk):
    movie = Movie.objects.get(pk=pk)
    favorite_movies = Favorite_Movie.objects.filter(userID=request.user.id).values_list('movieID', flat=True)
    context = {
        'movie': movie,
        'favorites': favorite_movies
    }
    return render(request, 'movies/movies_detail.html', context)


@login_required
def FavoriteMovieCreate(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie_cast = Casting.objects.filter(movieID=pk).first()
    form = FavoriteMovieForm(initial={'movieID': movie,
                                      'userID': request.user,
                                      'favActorID': movie_cast})
    form.fields['favActorID'].queryset = Casting.objects.filter(movieID=pk)
    if request.method == 'POST':
        form = FavoriteMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    context = {
        'form': form,
        'movie': movie
    }

    return render(request, 'movies/add_favorite.html', context)

def EditFavoriteMovie(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = FavoriteMovieForm(initial={'movieID': movie,
                                      'userID': request.user})
    form.fields['favActorID'].queryset = Casting.objects.filter(movieID=pk)
    if request.method == 'POST':
        form = FavoriteMovieForm(request.POST)
        if form.is_valid():
            Favorite_Movie.objects.filter(movieID=movie).delete()
            form.save()
            return redirect('/profile')
    context = {
        'form': form,
        'movie': movie
    }
    return render(request, 'movies/add_favorite.html', context)
    
def RemoveFavoriteMovie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie_instance = Favorite_Movie.objects.filter(movieID=movie).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

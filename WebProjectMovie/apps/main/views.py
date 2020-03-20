from django.shortcuts import render, redirect
from .models import Movie
from django.contrib.auth import authenticate, login

def home(request):
	movies = Movie.objects.all()
	context = {
		'movies': movies
	}
	return render(request, 'home.html', context)



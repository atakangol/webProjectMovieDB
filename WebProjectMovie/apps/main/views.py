from django.shortcuts import render, redirect
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def main(request):
	return render(request, 'main.html')

def movie_list(request):
	movies = Movie.objects.all()

	context = {
		'movies': movies
	}

	return render(request, 'main.html', context)

def loginn(request):
    #context = {'form' : form}
    context = {}
    return render(request, 'login.html', context)

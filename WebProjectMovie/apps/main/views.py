from django.shortcuts import render, redirect
from .models import Movie
from django.contrib.auth import authenticate, login

def main(request):
	movies = Movie.objects.all()
	context = {
		'movies': movies
	}
	return render(request, 'main.html', context)


def loginn(request):
    #context = {'form' : form}
    context = {}
    return render(request, 'login.html', context)

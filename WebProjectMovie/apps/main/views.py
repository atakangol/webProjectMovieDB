from django.shortcuts import render
from .models import Movie

def main(request):
	return render(request, 'main.html', {})

def movie_list(request):
	movies = Movie.objects.all()

	context = {
		'movies': movies
	}

	return render(request, 'main.html', context)

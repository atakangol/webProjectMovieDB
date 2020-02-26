from django.shortcuts import render
from .models import Movies

def main(request):
	return render(request, 'main.html', {})

def movie_list(request):
	movies = Movies.objects.all()

	context = {
		'movies': movies
	}

	return render(request, 'main.html', context)

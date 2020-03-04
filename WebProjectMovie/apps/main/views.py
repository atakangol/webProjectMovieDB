from django.shortcuts import render, redirect
from .models import Movies
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def main(request):
	return render(request, 'main.html')

def movie_list(request):
	movies = Movies.objects.all()

	context = {
		'movies': movies
	}

	return render(request, 'main.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'register.html', context)

def loginn(request):
    #context = {'form' : form}
    context = {}
    return render(request, 'login.html', context)
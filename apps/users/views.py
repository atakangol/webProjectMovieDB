from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from apps.main.models import Favorite_Movie, Movie

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('url_login')
            
    return render(request, 'register.html', {'form':form}) 

@login_required
def profile(request):
        favorites = Favorite_Movie.objects.filter(userID=request.user.id)
        movies = Movie.objects.all()
        context = {
                'favorites':favorites,
                'movies':movies
        }
        return render(request, 'profile.html', context)
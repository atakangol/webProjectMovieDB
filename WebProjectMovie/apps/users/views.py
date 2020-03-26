from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

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
        return render(request, 'profile.html')
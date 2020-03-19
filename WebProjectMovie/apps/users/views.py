from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('main')
            
    return render(request, 'register.html', {'form':form}) 

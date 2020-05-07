from django.shortcuts import render
from apps.main.models import *
from django.contrib.auth.decorators import user_passes_test

def check_admin(user):
   return user.is_superuser

@user_passes_test(check_admin)
def ReadApiView(request):    
    return render(request, 'readapi.html')

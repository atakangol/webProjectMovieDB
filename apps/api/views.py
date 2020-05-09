from django.shortcuts import render
from apps.main.models import *
from django.contrib.auth.decorators import user_passes_test

def check_admin(user):
   return user.is_superuser

@user_passes_test(check_admin)
def ReadApiView(request):    
    return render(request, 'readapi.html')

def run_script(request):
   if request.method == 'POST' and 'run_script' in request.POST:

    # import function to run
    from api_trials.api2db.py import #METHODS

    #We can call the functions

    # That is for if we want to redirect a user to a another page. 
    # return HttpResponseRedirect(reverse(app_name:view_name)
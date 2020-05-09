from django.shortcuts import render
from apps.main.models import *
from django.contrib.auth.decorators import user_passes_test
from .api2db import *
def check_admin(user):
   return user.is_superuser

@user_passes_test(check_admin)
def ReadApiView(request):
   
   if request.method == 'POST' and 'reset_db' in request.POST:
      delete_movies()
      delete_people()
      all_genres(delete=True)
      
      
      print("movies people and genres (and in betweens) reset, all deleted")

   if request.method == 'POST' and 'test_read' in request.POST:
      all_movies("apps/api/ids/test/film_ids.txt")
      all_people("apps/api/ids/test/people_ids.txt")
      print("tests added")
   
   if request.method == 'POST' and 'read_all' in request.POST:
      all_movies("apps/api/ids/popular/film_ids.txt")
      all_people("apps/api/ids/popular/people_ids.txt")
      print("all popular added")
   
   if request.method == 'POST' and 'read_new' in request.POST:
      all_movies("apps/api/ids/new/film_ids.txt")
      all_people("apps/api/ids/new/people_ids.txt")
      print("new films and people added")
   #print("aa")
   
   return render(request, 'readapi.html')
   
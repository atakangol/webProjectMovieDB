from django.shortcuts import render
import requests
import os,django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE","WebProjectMovie.settings")
django.setup()

import apps.main.models as m
#needs to be in /webProjectMovieDB/ to be run

api_key = "6d61b3e2ab08b90b76aba55d68fd4fac"
#dont know how to put secrets exactly

def all_genres(delete=True):
    if (delete):
        genres = m.Genre.objects.all()
        #print(genres)
        for genre in genres:
            #print(genre)
            genre.delete()

    genre_names = []
    genres = m.Genre.objects.all()
    for i in genres:
        genre_names.append(i.genreName)
    req = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key={}&language=en-US".format(api_key))

    response = req.json()
    #print(response)
    
    #print("all the genres in the database:\n")
    for i in response["genres"]:
        if(i["name"] not in genre_names):
            genre_names.append(i["name"])

    #print(genre_names)

    for i in  range(0,len(genre_names)):
        #print(genre_names[i])
        g = m.Genre(genreID =i+1,genreName =genre_names[i])
        g.save()

def top_films_txt():

    top_film_ids = []
    f = open("./api tests and trials/film_ids.txt","w")
    for i in range(1,6):


        req = requests.get("https://api.themoviedb.org/3/movie/popular?api_key={}&language=en-US&page={}".format(api_key,i))
        response = req.json()
        #print(response)
        for k in response["results"]:
            f.write(str(k["id"])+"\n")
            top_film_ids.append(k["id"])
            #print(k["id"])
            

    #print(len(top_film_ids))


    f.close()

def actors_txt():
    top_film_ids = []
    f = open("./api tests and trials/people_ids.txt","w")
    for i in range(1,6):


        req = requests.get("https://api.themoviedb.org/3/person/popular?api_key={}&language=en-US&page={}".format(api_key,i))
        response = req.json()
        #print(response)
        for k in response["results"]:
            f.write(str(k["id"])+"\n")
            top_film_ids.append(k["id"])
            #print(k["id"])
            

    #print(len(top_film_ids))


    f.close()
    




def add_actor(person_id):
    try:
        movie = m.Person.objects.get(personId=int(person_id))
    except:
        req = requests.get("https://api.themoviedb.org/3/person/{person_id}?api_key={api_key}&language=en-US".format(person_id=int(person_id),api_key=api_key))
        response = req.json()
        birth = response["birthday"]
        if(birth ==None):
            birth = datetime(1,1,1)
            
        try:
            path = response["profile_path"]
        except:
            path = None    
        p = m.Person(PersonId=int(person_id),Pname=response["name"],Pbirth=birth,Ppic = path)
        #print(p)
        p.save()
    
def add_actor_all(person_id,film_limit=30):
    try:
        new_person = m.Person.objects.get(PersonId=int(person_id))
    except:

        req = requests.get("https://api.themoviedb.org/3/person/{person_id}?api_key={api_key}&language=en-US".format(person_id=int(person_id),api_key=api_key))
        response = req.json()
        birth = response["birthday"]
        if(birth ==None):
            birth = datetime(1,1,1)
            
        try:
            path = response["profile_path"]
        except:
            path = None    
        new_person = m.Person(PersonId=int(person_id),Pname=response["name"],Pbirth=birth,Ppic = path)
        #print(new_person)
        new_person.save()
        
    req = requests.get("https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key={api_key}&language=en-US".format(person_id=int(person_id),api_key=api_key))
    response = req.json()
    crew = response["crew"]
    #print(crew)
    for k in crew:
        if (k["job"]) == "Director":
            add_movie(k["id"])
            break
    cast = response["cast"]
    #print(cast)
    count = 0
    for k in cast:
        if(count >= film_limit):
            break
        count += 1
        add_movie(k["id"],new_person)    

def add_movie(movie_id,person=None):
    try:
        movie = m.Movie.objects.get(movieID=int(movie_id))
    except:
        try:
            #print(movie_id,person)
            
            req = requests.get("https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}".format(movie_id=int(movie_id),api_key=api_key))
            response = req.json()
            crew = response["crew"]
            director = None
            for k in crew:
                if (k["job"]) == "Director":
                    try:
                        director = m.Person.objects.get(PersonId=k["id"])
                    except :
                        #print("direstor not found",k["id"],movie_id)
                        add_actor(k["id"])
                        #director=None
                        director = m.Person.objects.get(PersonId=k["id"])
                    break
            if ( director==None):
                return
            cast_ids=[]
            cast = response["cast"]
            for k in cast:
                cast_ids.append(k["id"])
            req = requests.get("https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}".format(movie_id=int(movie_id),api_key=api_key))
            response = req.json()
            genres = []
            temp = response["genres"]
            for i in temp:
                genres.append(i["name"])
            name = response["original_title"]
            path = response["poster_path"]
            date = response["release_date"]
            date = date.split("-")[0]
            new_movie =m.Movie(movieID = movie_id,movieName = name,movieYear = date,directorID = director,Mpic = path)
            new_movie.save()

            
            for genre_name in genres:
                genre = m.Genre.objects.get(genreName=genre_name)
                new_category = None
                new_category = m.Category(movieID =new_movie, genreID = genre)
                #print(new_category.movieID,new_category.genreID)
                new_category.save()
            

            if (person!=None):
                new_cast = None
            
                new_cast = m.Casting(personID=person,movieID=new_movie)
                new_cast.save()
        except:
            return

def delete_people():
    people = m.Person.objects.all()
    #print(genres)
    for person in people:
        #print(genre)
        person.delete()    
        
def delete_movies():
    movies = m.Movie.objects.all()
    #print(genres)
    for movie in movies:
        #print(genre)
        movie.delete()

def add_movie_credits(movie_id,cast_limit=50):
    try:
        try: 
            new_movie = m.Movie.objects.get(movieID=int(movie_id))
            
        except:
            add_movie(movie_id)
            new_movie = m.Movie.objects.get(movieID=int(movie_id))
        
        req = requests.get("https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}".format(movie_id=int(movie_id),api_key=api_key))
        response = req.json()        
        
        cast_ids=[]
        cast = response["cast"]
        #print(cast)
        for k in cast[:cast_limit]:
            cast_ids.append(k["id"])
        for cast_id in cast_ids:
            #print(cast_id)
            new_cast = None
            
            try:
                actor = m.Person.objects.get(PersonId = cast_id)
                
            except :
                #print("actor not found ", cast_id,movie_id)
                add_actor(cast_id)
                actor = m.Person.objects.get(PersonId = cast_id)
                #continue
            #order += 1
            new_cast = m.Casting(personID=actor,movieID=new_movie)
            new_cast.save()
        #print(int(movie_id)," done")
    except:
        return

def all_movies():
    f = open("./api tests and trials/film_ids.txt","r")
    for movie_id in f:
        #print(int(movie_id))
        add_movie_credits(int(movie_id),30)
    f.close

def all_people():
    f = open("./api tests and trials/people_ids.txt","r")
    for person_id in f:
        add_actor_all(int(person_id))
        
    f.close

if __name__ == '__main__':
    delete_movies()
    delete_people()
    all_genres(delete=True)

    
    all_movies()
    all_people()
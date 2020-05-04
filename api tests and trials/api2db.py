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

def all_genres():
    req = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key={}&language=en-US".format(api_key))

    response = req.json()
    #print(response)
    genre_names = []
    #print("all the genres in the database:\n")
    for i in response["genres"]:
        genre_names.append(i["name"])

    #print(genre_names)

    for i in  range(0,len(genre_names)):
        #print(genre_names[i])
        g = m.Genre(genreID =i+1,genreName =genre_names[i])
        g.save()

def top_films_txt():

    top_film_ids = []
    f = open("./api tests and trials/film_ids.txt","w")
    for i in range(1,11):


        req = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key={}&language=en-US&page={}".format(api_key,i))
        response = req.json()
        #print(response)
        for k in response["results"]:
            f.write(str(k["id"])+"\n")
            top_film_ids.append(k["id"])
            #print(k["id"])
            

    #print(len(top_film_ids))


    f.close()

def actors_txt():
    f = open("./api tests and trials/film_ids.txt","r")
    people_ids = []
    for movie_id in f:
        #print(int(movie_id))

        req = requests.get("https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}".format(movie_id=int(movie_id),api_key=api_key))
        response = req.json()
        
        crew = response["crew"]
        for k in crew:

            if (k["job"]) == "Director":
                #print(k["id"])
                
                if (k["id"] not in people_ids):
                    people_ids.append(k["id"])
                    break
        #print("--")
        
        cast = response["cast"]
        if (len(cast)==0):
            print(movie_id)
            continue
        '''
        for k in range(0,min(15,len(cast))):
            if (cast[k]["id"] not in people_ids):
                people_ids.append(cast[k]["id"])
            
        '''
        for k in cast:
            if (k["id"] not in people_ids):
                people_ids.append(k["id"])
        
        
    #print(len(people_ids))
    f.close()
    f1 = open("./api tests and trials/people_ids.txt","a")
    for i in people_ids:
        f1.write(str(i)+"\n")
    f1.close()

def actors_db():
    f = open("./api tests and trials/people_ids.txt","r")
    count = 0
    for person_id in f:
        count += 1

        req = requests.get("https://api.themoviedb.org/3/person/{person_id}?api_key={api_key}&language=en-US".format(person_id=int(person_id),api_key=api_key))
        response = req.json()
        
        if(response["birthday"] == None):
            continue 
        #print(response["name"])
        req = requests.get("https://api.themoviedb.org/3/person/{person_id}/images?api_key={api_key}".format(person_id=int(person_id),api_key=api_key))
        pic = req.json()
        #print(pic)
        pp= None
        if (0!=len(pic["profiles"])):

            #print(pic["profiles"][0]["file_path"])
            pp = pic["profiles"][0]["file_path"]
        p = m.Person(PersonId=int(person_id),Pname=response["name"],Pbirth=response["birthday"],Ppic = pp)
        #print(p)
        p.save()

    f.close()

def add_actor(person_id):

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
    print(p)
    p.save()
    

def movies_db():#movies casting categories
    #all_people = m.Person.objects.all()
    #all_genre = m.Genre.objects.all()
    f = open("./api tests and trials/film_ids.txt","r")

    for movie_id in f:
    #movie_id = 278
    
        req = requests.get("https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}".format(movie_id=int(movie_id),api_key=api_key))
        response = req.json()
        
        crew = response["crew"]
        for k in crew:
            if (k["job"]) == "Director":
                try:
                    director = m.Person.objects.get(PersonId=k["id"])
                except :
                    print("direstor not found",k["id"],movie_id)
                    add_actor(k["id"])
                    #director=None
                    director = m.Person.objects.get(PersonId=k["id"])
        
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
        #print(new_movie)
        #print(cast_ids)
        #print(genres)
        for genre_name in genres:
            genre = m.Genre.objects.get(genreName=genre_name)
            new_category = None
            new_category = m.Category(movieID =new_movie, genreID = genre)
            #print(new_category.movieID,new_category.genreID)
            new_category.save()
        order = 0
        for cast_id in cast_ids:
            new_cast = None
            try:
                actor = m.Person.objects.get(PersonId = cast_id)
                
            except :
                print("actor not found ", cast_id,movie_id)
                continue
            order += 1
            new_cast = m.Casting(order=order,personID=actor,movieID=new_movie)
            new_cast.save()
        print(int(movie_id)," done")
    f.close()

if __name__ == '__main__':
    """
    try:
        p = m.Person.objects.get(PersonId=504)
    except :
       p=None
    #print(p)
    
    req = requests.get("https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}".format(movie_id=int(278),api_key=api_key))
    response = req.json()
    name = response["original_title"]
    path = response["poster_path"]
    date = response["release_date"]
    date = date.split("-")[0]
    print(date)
    """
    #all_genres()
    #actors_db()
    movies_db()
    #test = m.Movie(movieID = 666,movieName = "testt",movieYear = 1998,directorID = None,Mpic = "dfgdegd")
    #print(test)
    #add_actor(2436936)
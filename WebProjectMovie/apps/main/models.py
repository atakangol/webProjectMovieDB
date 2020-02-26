from django.db import models


class Person(models.Model):
    PersonId = models.IntegerField(unique=True)
    Pname = models.CharField(max_length=50)
    Pbirth = models.DateTimeField()

    def __str__(self):
        return self.Pname

class Movie(models.Model):
    movieID = models.IntegerField(unique=True) ####
    movieName = models.CharField(max_length=30)
    movieYear = models.IntegerField()
    directorID = models.ForeignKey(Person, on_delete=models.CASCADE)####

    def __str__(self):
        return self.movieName

class Genre(models.Model):
    genreID = models.IntegerField()
    genreName = models.CharField(max_length=20)

    def __str__(self):
        return self.genreName

class Category(models.Model):
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genreID = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return (self.movieID, self.genreID)

class Casting(models.Model):
     order = models.IntegerField(unique=True)
     personID = models.ForeignKey(Person, on_delete=models.CASCADE)
     movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)

     def __str__(self):
         return self.order

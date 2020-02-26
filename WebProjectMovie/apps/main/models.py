from django.db import models


class People(models.Model):
    peopleId = models.IntegerField(unique=True)
    Pname = models.CharField(max_length=50)
    Pbirth = models.DateTimeField()

    def __str__(self):
        return self.Pname

class Movies(models.Model):
    movieID = models.IntegerField(unique=True) ####
    movieName = models.CharField(max_length=30)
    movieYear = models.IntegerField()
    directorID = models.ForeignKey(People, on_delete=models.CASCADE)####

    def __str__(self):
        return self.movieName

class Genres(models.Model):
    genreID = models.IntegerField()
    genreName = models.CharField(max_length=20)

    def __str__(self):
        return self.genreName

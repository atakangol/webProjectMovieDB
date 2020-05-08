from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls.base import reverse


class Person(models.Model):
    PersonId = models.IntegerField(unique=True)
    Pname = models.CharField(max_length=50)
    Pbirth = models.DateTimeField()
    Ppic = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.Pname


class Movie(models.Model):
    movieID = models.IntegerField(unique=True)
    movieName = models.CharField(max_length=30)
    movieYear = models.IntegerField()
    directorID = models.ForeignKey(Person, on_delete=models.CASCADE)
    Mpic = models.CharField(null=True, max_length=100)

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
    # order = models.IntegerField(unique=False)
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.personID)


class Favorite_Movie(models.Model):
    movieID = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    favActorID = models.ForeignKey(Casting, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movieID)

    def get_absolute_url(self):
        return reverse('movies:movie_detail', kwargs={'pk': self.pk})


class Favorite_Actor(models.Model):
    PersonID = models.ForeignKey(Person, on_delete=models.CASCADE)
    UserName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return (self.PersonID, self.UserID)


class List(models.Model):
    ListOwner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ListID = models.IntegerField(unique=True)
    Date = models.DateTimeField()
    Rating = models.IntegerField()
    Public = models.BooleanField()

    def __str__(self):
        return (self.ListOwner, self.ListID)


class List_Content(models.Model):
    ListID = models.ForeignKey(List, on_delete=models.CASCADE)
    MovieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    Order = models.IntegerField()

    def __str__(self):
        return (self.ListID)

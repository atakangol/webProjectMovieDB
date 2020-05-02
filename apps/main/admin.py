from django.contrib import admin
from . import models


# Newest way -------------------------
@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Person)
class PeopleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Genre)
class CommentGenres(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CommentGenres(admin.ModelAdmin):
    pass


@admin.register(models.Casting)
class CommentGenres(admin.ModelAdmin):
    pass


@admin.register(models.List)
class CommentGenres(admin.ModelAdmin):
    pass


@admin.register(models.Favorite_Actor)
class CommentGenres(admin.ModelAdmin):
    pass


@admin.register(models.Favorite_Movie)
class CommentGenres(admin.ModelAdmin):
    pass


@admin.register(models.List_Content)
class CommentGenres(admin.ModelAdmin):
    pass

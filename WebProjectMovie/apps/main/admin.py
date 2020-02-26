from django.contrib import admin
from . import models

# Newest way -------------------------
@admin.register(models.Movies)
class MovieAdmin(admin.ModelAdmin):
	pass

@admin.register(models.People)
class PeopleAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Genres)
class CommentGenres(admin.ModelAdmin):
    pass

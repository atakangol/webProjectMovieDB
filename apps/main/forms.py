from django.forms import ModelForm
from apps.main.models import Favorite_Movie
from django import forms


class FavoriteMovieForm(ModelForm):
    class Meta:
        model = Favorite_Movie
        fields = ('favActorID', 'movieID', 'userID', 'movieName')
        widgets =  {'movieID': forms.HiddenInput(),
                    'userID': forms.HiddenInput(),
                    'movieName': forms.HiddenInput()}
        labels = {
            'favActorID': 'Who is you favorite actor in this movie ?',
        }

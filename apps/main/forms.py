from django.forms import ModelForm
from apps.main.models import Favorite_Movie


class MovieForm(ModelForm):
    class Meta:
        model = Favorite_Movie
        exclude = ('movieID', 'user')

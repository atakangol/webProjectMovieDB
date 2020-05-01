from django.forms import ModelForm
from apps.main.models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ()

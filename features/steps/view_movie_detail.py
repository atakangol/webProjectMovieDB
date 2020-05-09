from behave import *

use_step_matcher("parse")


@when('I view the details for movies "{movie_name}"')
def step_impl(context, movie_name):
   # from apps.main.models import Favorite_Movie
   # movie = Favorite_Movie.objects.get(movieID=2)
    context.browser.visit(context.get_url('/details/2'))#, movie.pk))



from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")


@given('Exists movie registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from apps.main.models import Favorite_Movie
    for row in context.table:
        movie = Favorite_Movie(user=user)
        for heading in row.headings:
            setattr(movie, heading, row[heading])
        movie.save()


@when(u'I register movie')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/addfavorite'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()


@then(u'I\'m viewing the details page for movies')
def step_impl(context):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from apps.main.models import Favorite_Movie
    movie = Favorite_Movie.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(movie)


@then(u'There are {count:n} movies')
def step_impl(context, count):
    from apps.main.models import Favorite_Movie
    assert count == Favorite_Movie.objects.count()

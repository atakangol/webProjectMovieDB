from behave import *
from selenium.webdriver.support.select import Select

use_step_matcher("parse")

@when(u'I register favorite movie')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/addfavorite/1'))
        form = context.browser.find_by_tag('form').first
        dropdown = Select(context.browser.find_by_id('id_favActorID'))
        #for heading in row.headings:
        #        dropdown.select_by_visible_text(row[heading])
        #form.find_by_value('addfav').first.click()

@then(u'There are {count:n} movies')
def step_impl(context, count):
    from apps.main.models import Favorite_Movie
    assert count == Favorite_Movie.objects.count()

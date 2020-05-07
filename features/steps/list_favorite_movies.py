from behave import *

use_step_matcher("parse")


@when('I list movies')
def step_impl(context):
    context.browser.visit(context.get_url('/profile'))


@then('I\'m viewing a list containing')
def step_impl(context):
    movie_links = context.browser.find_by_css('div#content article div div a')
    for i, row in enumerate(context.table):
        assert row['movieName'] == movie_links[i].text


@step('The list contains {count:n} movies')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#content article div div a'))

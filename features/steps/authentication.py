from behave import *
from datetime import datetime

use_step_matcher("parse")


@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url(''))
    assert context.browser.is_text_present('Login')


@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    from apps.main.models import Movie, Person, Casting
    User.objects.create_user(username=username, email='user@example.com', password=password)
    person=Person.objects.create(PersonId=1, Pname="Luke Skywalker")
    movie=Movie.objects.create(movieID=1, movieName="Star Wars", movieYear=1977, directorID=person, Mpic="x")
    Casting.objects.create(movieID=movie, personID=person)


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/login'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()


@then('There is no "{link_text}" link available')
def step_impl(context, link_text):
    assert context.browser.is_element_not_present_by_xpath('//a[text()="' + link_text + '"]')

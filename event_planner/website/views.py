from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):
    """
        A function to render the welcome page.
    Args:
        request (request): the request object

    Returns:
        HttpResponse: Message to the user
    """
    return HttpResponse("Welcome to the Event Planner!")


def get_date(request):
    """
        A function to render the date page.
    Args:
        request (request): the request object

    Returns:
        HttpResponse: Message to the user
    """
    return HttpResponse("This page will show the date of the event " + str(datetime.now()))


def about_me(request):
    """
        A function to render the about me page.
    Args:
        request (request): the request object

    Returns:
        HttpResponse: Message to the user
    """
    name = "Megan"
    age = 21
    profession = "Student"
    country_of_origin = "Nigeria"

    return HttpResponse("My name is " + name + ", I am " + str(age) + " years old, I am a " + profession + " from " +
                        country_of_origin)

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

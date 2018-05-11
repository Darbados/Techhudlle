from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Leagues
# Create your views here.


def index(request):
    return HttpResponse("The index page is working.")

def prematch(request):
    all_leagues = Leagues.objects.all()

    response_text = ""

    for l in all_leagues:
        response_text += "{0}-{1}-{2}<br>".format(l.title,l.country,l.created_at)

    return HttpResponse(response_text)
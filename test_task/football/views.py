from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views import View
from .models import Leagues, Teams, Events
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
import json


def index(request):
    return HttpResponse("The index page is working.")


class SaveInDatabase(View):
    """
    For this view, the only allowed method is POST, as it plays the roll of exchange in the chain, it will only receive
    POST requests from the scraper which is the publisher and it will store the new records in the database, so the
    subscriber ( the FE ) will be able to display them when make request to the JSON API
    """

    def get(self, request):
        return JsonResponse({
           'msg_type': 'FAIL',
           'msg_info': 'Only POST requests are allowed'
        })

    def post(self, request):
        data = json.loads(request.body)

        for date, events in data.items():
            for league in events:
                country = ""
                league_title = league.split(',')[0] if ',' in league else league

                if len(data[date][league]):
                    country = data[date][league][0]['country']

                # Fill the leagues table with data
                if Leagues.objects.filter(league_title=league_title).exists():
                    pass
                else:
                    if league_title != '' and country != '':
                        l = Leagues.objects.create(league_title=league_title, country=country, added_at=timezone.now())
                        l.save()
                        print(date, league_title, country)
                    else:
                        pass

                # Fill the teams & events tables with data
                if len(data[date][league]):
                    for event in data[date][league]:
                        team1 = event["home_team"]
                        team2 = event["away_team"]
                        event_title = event["event_name"]
                        start_time = event["start_date"]

                        if not Teams.objects.filter(title=team1).exists():
                            t1 = Teams.objects.create(title=team1, country=country, created_at=timezone.now())
                            t1.save()
                            t2 = Teams.objects.create(title=team2, country=country, created_at=timezone.now())
                            t2.save()
                        else:
                            pass

                        if not Events.objects.filter(title=event_title, start_time=start_time).exists():
                            e = Events.objects.create(title=event_title, country=country, start_time=start_time)
                            e.save()

        return JsonResponse({
           'msg_type': 'Success',
           'msg_info': 'We have data to save into the database'
        })


def prematch(request):
    all_leagues = Leagues.objects.all()

    response_text = ""

    for l in all_leagues:
        response_text += "{0}-{1}-{2}<br>".format(l.league_title,l.country,l.added_at)

    return HttpResponse(response_text)


class EventsAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request):
        events = Events.objects.all()

        events_dict = {}
        for index,e in enumerate(events):
            events_dict[index+1] = {'event_title': e.title, 'start_time': e.start_time, 'country': e.country}

        return Response(events)
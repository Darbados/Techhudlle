from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views import View
from rest_framework.views import APIView
from .models import Leagues, Teams, EventsPremach, EventsLive, EventsFinished
from datetime import datetime, timedelta
from .serializers import EventsPrematchSerializer, EventsLiveSerializer, EventsFinishedSerializer, TeamsSerializer, LeaguesSerializer
from .handlers import handle_received_source
import json


def index(request):
    template = 'football/index.html'
    context = {'message': 'Welcome to the home page'}
    return render(request, template, context)


class SaveInDatabasePrematch(View):
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

        handle_received_source(data, Leagues, Teams, EventsPremach, timezone, datetime, 'prematch')

        return JsonResponse({
           'msg_type': 'Success',
           'msg_info': 'We have data to save into the database'
        })


class SaveInDatabaseLive(View):
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
        period = 'live'

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
                        l = Leagues.objects.create(league_title=league_title, country=country,
                                                      added_at=timezone.now())
                        l.save()
                    else:
                        pass

                # Fill the teams & events tables with data
                if len(data[date][league]):
                    for event in data[date][league]:
                        team1 = event["home_team"]
                        team2 = event["away_team"]
                        event_title = event["event_name"]
                        start_time = event["start_date"]

                        event_status = event["status"]
                        live_minute = 0
                        live_score_home = 0
                        live_score_away = 0

                        if period == 'live':
                            live_minute = event["liveScore"]["live_minute"]
                            live_score_home = event["liveScore"]["home_team_score"]
                            live_score_away = event["liveScore"]["away_team_score"]
                        elif period == 'finished':
                            live_score_home = event["liveScore"]["home_team_score"]
                            live_score_away = event["liveScore"]["away_team_score"]

                        if not Teams.objects.filter(title=team1).exists():
                            t1 = Teams.objects.create(title=team1, country=country, league=league_title,
                                                         created_at=timezone.now())
                            t1.save()
                            t2 = Teams.objects.create(title=team2, country=country, league=league_title,
                                                         created_at=timezone.now())
                            t2.save()
                        else:
                            pass

                        if EventsLive.objects.filter(title=event_title).exists():
                            ev = EventsLive.objects.get(title=event_title)
                            if ev.live_minute != live_minute:
                                ev.live_minute = live_minute
                                ev.save()
                            if ev.live_score_home != live_score_home:
                                ev.live_score_home = live_score_home
                                ev.save()
                            if ev.live_score_away != live_score_away:
                                ev.live_score_away = live_score_away
                                ev.save()
                        else:
                            e = EventsLive.objects.create(title=event_title, country=country, status=event_status,
                                                         live_minute=live_minute, live_score_home=live_score_home,
                                                         live_score_away=live_score_away,
                                                         created_at=timezone.now())
                            e.save()

        return JsonResponse({
           'msg_type': 'Success',
           'msg_info': 'We have data to save into the database'
        })


class SaveInDatabaseFinished(View):
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
        period = 'finished'

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
                        l = Leagues.objects.create(league_title=league_title, country=country,
                                                      added_at=timezone.now())
                        l.save()
                    else:
                        pass

                # Fill the teams & events tables with data
                if len(data[date][league]):
                    for event in data[date][league]:
                        team1 = event["home_team"]
                        team2 = event["away_team"]
                        event_title = event["event_name"]
                        start_time = event["start_date"]

                        event_status = event["status"]
                        live_minute = 0
                        live_score_home = 0
                        live_score_away = 0

                        if period == 'finished':
                            live_score_home = event["liveScore"]["home_team_score"]
                            live_score_away = event["liveScore"]["away_team_score"]

                        if not Teams.objects.filter(title=team1).exists():
                            t1 = Teams.objects.create(title=team1, country=country, league=league_title,
                                                         created_at=timezone.now())
                            t1.save()
                            t2 = Teams.objects.create(title=team2, country=country, league=league_title,
                                                         created_at=timezone.now())
                            t2.save()
                        else:
                            pass

                        if not EventsFinished.objects.filter(title=event_title, start_time=start_time).exists():
                            e = EventsFinished.objects.create(title=event_title, country=country, status=event_status,
                                                         start_time=start_time, final_score_home=live_score_home, final_score_away=live_score_away)
                            e.save()

        return JsonResponse({
           'msg_type': 'Success',
           'msg_info': 'We have data to save into the database'
        })


def prematch(request):
    template = 'football/prematch_events.html'
    context = {'title': 'Prematch events'}
    return render(request, template, context)


def live(request):
    template = 'football/live_events.html'
    context = {'title': 'Live events'}
    return render(request, template, context)


def finished(request):
    template = 'football/finished_events.html'
    context = {'title': 'Finished events'}
    return render(request, template, context)


def teams(request):
    template = 'football/teams.html'
    context = {'title': 'Teams page'}
    return render(request, template, context)


def leagues(request):
    template = 'football/leagues.html'
    context = {'title': 'Leagues page'}
    return render(request, template, context)


class EventsPrematchAPI(APIView):

    def get(self, request):
        events = EventsPremach.objects.filter(start_time__gte=timezone.now())

        serializer = EventsPrematchSerializer(events, many=True)

        return JsonResponse(serializer.data, safe=False)


class EventsLiveAPI(APIView):

    def get(self, request):
        events = EventsLive.objects.filter(created_at__gt=(datetime.now() - timedelta(minutes=105)))

        serializer = EventsLiveSerializer(events, many=True)

        return JsonResponse(serializer.data, safe=False)


class EventsFinishedAPI(APIView):

    def get(self, request):
        events = EventsFinished.objects.all()

        serializer = EventsFinishedSerializer(events, many=True)

        return JsonResponse(serializer.data, safe=False)


class TeamsAPI(APIView):

    def get(self, request):
        events = Teams.objects.all().order_by('league')

        serializer = TeamsSerializer(events, many=True)

        return JsonResponse(serializer.data, safe=False)


class LeaguesAPI(APIView):

    def get(self, request):
        events = Leagues.objects.all().order_by('country')

        serializer = LeaguesSerializer(events, many=True)

        return JsonResponse(serializer.data, safe=False)
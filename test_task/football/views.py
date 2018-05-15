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

        handle_received_source(data, Leagues, Teams, EventsFinished, timezone, datetime, 'live')

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

        handle_received_source(data, Leagues, Teams, EventsFinished, timezone, datetime, 'finished')

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


def about(request):
    template = 'football/about.html'
    context = {'title': 'About page'}
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
        events = Teams.objects.all()

        serializer = TeamsSerializer(events, many=True)

        return JsonResponse(serializer.data, safe=False)


class LeaguesAPI(APIView):

    def get(self, request):
        events = Leagues.objects.all()

        serializer = LeaguesSerializer(events, many=True)

        return JsonResponse(serializer.data, safe=False)
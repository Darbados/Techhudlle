from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from .models import EventsPremach, EventsLive, EventsFinished, Teams, Leagues


class EventsPrematchSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventsPremach
        fields = ('id', 'title', 'country', 'status', 'start_time')


class EventsLiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventsLive
        fields = ('id', 'title', 'country', 'status', 'live_minute', 'live_score_home', 'live_score_away', 'created_at', 'event_id')


class EventsFinishedSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventsFinished
        fields = ('id', 'title', 'country', 'status', 'start_time', 'final_score_home', 'final_score_away')


class TeamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teams
        fields = ('id', 'title', 'country', 'league', 'created_at')


class LeaguesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leagues
        fields = ('id', 'league_title', 'country', 'added_at')
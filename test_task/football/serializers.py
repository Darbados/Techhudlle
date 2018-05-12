from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from .models import EventsPremach, EventsLive, EventsFinished, Teams, Leagues


class EventsPrematchSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventsPremach
        fields = '__all__'


class EventsLiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventsLive
        fields = '__all__'


class EventsFinishedSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventsFinished
        model = EventsFinished
        fields = '__all__'


class TeamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teams
        fields = ('id', 'title', 'country', 'created_at')


class LeaguesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leagues
        fields = ('id', 'title', 'country', 'created_at')
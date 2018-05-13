from django.contrib import admin

from .models import Leagues, Teams, EventsLive, EventsPremach, EventsFinished


class LeaguesAdmin(admin.ModelAdmin):
    list_display = ('id','league_title', 'country', 'added_at')


class TeamsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'country', 'league', 'created_at')


class EventsPrematchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'status', 'start_time')


class EventsLiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'status', 'live_minute', 'live_score_home', 'live_score_away')


class EventsFinishedAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'status', 'start_time', 'final_score_home', 'final_score_away')


admin.site.register(Leagues, LeaguesAdmin)
admin.site.register(Teams, TeamsAdmin)
admin.site.register(EventsPremach, EventsPrematchAdmin)
admin.site.register(EventsLive, EventsLiveAdmin)
admin.site.register(EventsFinished, EventsFinishedAdmin)

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^prematch/$', views.prematch, name='prematch_events'),
    url(r'^live/$', views.live, name='live_events'),
    url(r'^finished/$', views.finished, name='finished_events'),
    url(r'^teams/$', views.teams, name='all_teams'),
    url(r'^leagues/$', views.leagues, name='all_leagues'),
    url(r'^about/$', views.prematch, name='about'),
    url(r'^save_in_database_prematch/$', views.SaveInDatabasePrematch.as_view(), name='save_in_database_prematch'),
    url(r'^save_in_database_live/$', views.SaveInDatabaseLive.as_view(), name='save_in_database_live'),
    url(r'^save_in_database_finished/$', views.SaveInDatabaseFinished.as_view(), name='save_in_database_finished'),
    url(r'^api_events_prematch/$', views.EventsPrematchAPI.as_view()),
    url(r'^api_events_live/$', views.EventsLiveAPI.as_view()),
    url(r'^api_events_finished/$', views.EventsFinishedAPI.as_view()),
    url(r'^api_teams/$', views.TeamsAPI.as_view()),
    url(r'^api_leagues/$', views.LeaguesAPI.as_view()),
]
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^prematch/$', views.prematch, name='prematch'),
    url(r'^save_in_database/$', views.SaveInDatabase.as_view(), name='save_in_database'),
    url(r'^api_events/$', views.EventsAPI.as_view()),
]
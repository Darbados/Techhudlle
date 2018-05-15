"""
File with helper methods
"""


def handle_received_source(source, league_obj, team_obj, event_obj, time_func, date_func, period):
    for date, events in source.items():
        for league in events:
            country = ""
            league_title = league.split(',')[0] if ',' in league else league
    
            if len(source[date][league]):
                country = source[date][league][0]['country']
    
            # Fill the leagues table with source
            if league_obj.objects.filter(league_title=league_title).exists():
                pass
            else:
                if league_title != '' and country != '':
                    l = league_obj.objects.create(league_title=league_title, country=country, added_at=time_func.now())
                    l.save()
                else:
                    pass
    
            # Fill the teams & events tables with source
            if len(source[date][league]):
                for event in source[date][league]:
                    team1 = event["home_team"]
                    team2 = event["away_team"]
                    event_title = event["event_name"]
                    start_time = event["start_date"]
                    event_status = event["status"]

                    if not team_obj.objects.filter(title=team1).exists():
                        t1 = team_obj.objects.create(title=team1, country=country, league=league_title,
                                                  created_at=time_func.now())
                        t1.save()
                        t2 = team_obj.objects.create(title=team2, country=country, league=league_title,
                                                  created_at=time_func.now())
                        t2.save()
                    else:
                        pass
    
                    if period == 'prematch':
                        if not event_obj.objects.filter(title=event_title, start_time=start_time).exists():
                            e = event_obj.objects.create(title=event_title, country=country, status=event_status,
                                                         start_time=start_time)
                            e.save()
                        else:
                            continue
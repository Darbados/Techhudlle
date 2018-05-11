import json, os, sys

def read_json(filename):
    with open(filename, 'r') as fp:
        data = json.load(fp)
        for date, events in data.items():
            for league in events:
                country = ""
                league_title = league.split(',')[0] if ',' in league else league

                if len(data[date][league]):
                    country = data[date][league][0]['country']
                print(date, league_title, country)

read_json('publisher_source/results/soccer_prematch.json')
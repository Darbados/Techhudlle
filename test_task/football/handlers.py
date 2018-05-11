import json, os, sys

BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(BASEPATH)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_task.test_task.settings')

import django
django.setup()


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
import datetime
import json

import requests

from pga_tour_data.db.orm import add_tournaments


def parse_tournament_date(date):
    return datetime.datetime.strptime(date[:10], "%Y-%m-%d")


def get_tournaments():
    tournaments = []
    years = range(1995, 2020)
    for year in years:
        r = requests.get(
            "https://statdata.pgatour.com/historicalschedules/r/{}/historicalschedule.json"
            .format(year)
        )
        data = json.loads(r.content)
        tournaments += [{'tournament_year_id': tournament['ID'],
                         'tournament_id': tournament['PERM_NUM'],
                         'year': int(tournament['YEAR']),
                         'start_date': parse_tournament_date(tournament['START_DATE']),
                         'end_date': parse_tournament_date(tournament['END_DATE']),
                         'tournament_name': tournament['NAME'],
                         'course_id': tournament['COURSE_NUMBER'],
                         'course_name': tournament['COURSE_NAME'],
                         'country': tournament['COUNTRY'],
                         'state': tournament['STATE'],
                         'city': tournament['CITY'],
                         'purse': int(tournament['PURSE']),
                         'major': True if tournament['TRN_TYPE'] == 'MJR' else False}
                        for tournament in data['data']]
    return tournaments


if __name__ == '__main__':
    tournaments = get_tournaments()
    add_tournaments(tournaments)

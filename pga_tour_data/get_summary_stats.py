import json

import requests

import pga_tour_data.utils
from pga_tour_data.db.orm import query_pandas, add_summary_stats


def get_player_stats(player_id, year):
    r = requests.get("https://statdata.pgatour.com/players/{}/{}stat.json".format(player_id, year))
    data = json.loads(r.content)
    player_data = data['plrs'][0]
    return player_data


def parse_player_stats(player_data):
    player_data['years'][0]['tours'][0]['statCats'] = {x['catName']: x['stats']
                                                       for x in
                                                       player_data['years'][0][
                                                           'tours'][0][
                                                           'statCats']}
    for k in player_data['years'][0]['tours'][0]['statCats'].keys():
        player_data['years'][0]['tours'][0]['statCats'][k] = {x['statID']: x
                                                              for x in
                                                              player_data['years'][0]['tours'][0]['statCats'][k]}

    return player_data['years'][0]['tours'][0]['statCats']


if __name__ == '__main__':
    summary_stats = []
    for player_num in query_pandas(
            "SELECT player_id FROM players"
    )['player_id'].values:
        stats = {}
        player_num = pga_tour_data.utils.pad_with_zeroes(str(player_num))
        for year in [2012, 2013, 2014, 2015, 2016, 2017, 2018]:
            try:
                stats[year] = parse_player_stats(get_player_stats(player_num, year))
            except json.decoder.JSONDecodeError:
                stats[year] = {}
                print(player_num, year)
            except Exception:
                stats[year] = {}
                print(player_num, year, Exception)
        summary_stats.append({'player_id': player_num, 'stats': stats})
    add_summary_stats(summary_stats)

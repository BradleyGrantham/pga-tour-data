import json
import time

import requests

from pga_tour_data.db.orm import query_pandas, add_stat_names, add_player_stats


def get_player_stats(player_id):
    r = requests.get("https://statdata.pgatour.com/players/{}/r_recap.json"
                     .format(player_id))
    data = json.loads(r.content)
    player_data = data['plr']['tours'][0]
    assert player_data['tourCodeLC'] == 'r'

    player_data = parse_player_stats(player_data)

    return player_data


def parse_player_stats(player_data):
    player_data = {int(x['year']): x for x in player_data['years']}

    for year in player_data.keys():
        player_data[year] = {
            x['trn']['permNum']: x
            for x in player_data[year]['trnDetails']}

        for tournament in player_data[year].keys():
            player_data[year][tournament]['scr']['rounds'] = {
                int(x['rndNum']): x for x in
                player_data[year][tournament]['scr']['rounds']
            }

            player_data[year][tournament]['stats'] = (
                player_data[year][tournament]['profiles'][0]['stats']
            )

            player_data[year][tournament]['stats'] = {
                x['stid']: x['stValue'] for x in
                player_data[year][tournament]['stats']
            }

    return player_data


def get_stat_names():
    # use Rory McIlroy as the standard for this
    r = requests.get("https://statdata.pgatour.com/players/28237/r_recap.json")
    data = json.loads(r.content)
    stat_mappings = data['statList']
    stat_mappings = [{'stat_id': x['stid'],
                      'stat_name': x['stName']} for x in stat_mappings]
    return stat_mappings


if __name__ == '__main__':
    stat_names = get_stat_names()
    add_stat_names(stat_names, merge=True)

    stats = []
    for player_num in query_pandas(
            "SELECT player_id FROM players"
    )['player_id'].values:
        try:
            stats.append({'player_id': player_num,
                          'stats': get_player_stats(player_num)})
        except json.decoder.JSONDecodeError:
            print(player_num)
        except Exception:
            print(player_num, 'different_exception')
        time.sleep(6)
    add_player_stats(stats)

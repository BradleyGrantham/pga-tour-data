import json

import requests

from pga_tour_data.db.orm import add_players


def get_player_names_and_ids(year):
    r = requests.get("https://statdata.pgatour.com/r/stats/{}/02671.json"
                     .format(year))
    data = json.loads(r.content)
    player_details = data['tours'][0]['years'][0]['stats'][0]['details']
    info = [{'plrNum': plr['plrNum'],
             'firstName': plr['plrName']['first'],
             'lastName': plr['plrName']['last']}
            for plr in player_details]
    return info


if __name__ == '__main__':
    players = (get_player_names_and_ids(2012)
               + get_player_names_and_ids(2013)
               + get_player_names_and_ids(2014)
               + get_player_names_and_ids(2015)
               + get_player_names_and_ids(2016)
               + get_player_names_and_ids(2017)
               + get_player_names_and_ids(2018))
    players = {int(player['plrNum']): {'player_id': int(player['plrNum']),
                                       'first_name': player['firstName'],
                                       'last_name': player['lastName']}
               for player in players}
    add_players([x for x in players.values()])

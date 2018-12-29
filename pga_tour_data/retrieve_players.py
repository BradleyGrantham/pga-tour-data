import json

import requests

from pga_tour_data.db.orm import add_players


def get_players():
    r = requests.get("https://statdata.pgatour.com/players/player.json")
    data = json.loads(r.content)
    player_details = data['plrs']
    players = [{'player_id': plr['pid'],
             'first_name': plr['nameF'],
             'last_name': plr['nameL'],
             'nationality': plr['ct'],
             'years_on_tour': [int(x) for x in plr['yrs']]}
            for plr in player_details]
    return players


if __name__ == '__main__':
    players = get_players()
    add_players(players)

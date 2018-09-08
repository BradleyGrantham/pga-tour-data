import json

import requests

import src.constants as constants
from src.mongodb_methods import update_collection


def get_player_names_and_ids(year):
    r = requests.get("https://statdata.pgatour.com/r/stats/{}/02671.json".format(year))
    data = json.loads(r.content)
    player_details = data['tours'][0]['years'][0]['stats'][0]['details']
    info = [{'plrNum': plr['plrNum'], 'firstName': plr['plrName']['first'], 'lastName': plr['plrName'][
        'last']} for
            plr in
            player_details]
    return info


if __name__ == '__main__':
    players = get_player_names_and_ids(2018)
    for player in players:
        update_collection(player, database=constants.DATABASE_PGATOURSTATS, collection=constants.COLLECTION_NAMESANDIDS)

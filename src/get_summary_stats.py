import json

import requests

import src.constants as constants
from src.mongodb_methods import update_collection, read_field_from_collection


def get_player_stats(player_id, year):
    r = requests.get("https://statdata.pgatour.com/players/{}/{}stat.json".format(player_id, year))
    data = json.loads(r.content)
    player_data = data['plrs'][0]
    return player_data


if __name__ == '__main__':
    for player_num in read_field_from_collection('plrNum', database=constants.DATABASE_PGATOURSTATS,
                                                 collection=constants.COLLECTION_NAMESANDIDS):
        stats = get_player_stats(player_num, '2018')
        update_collection(stats, database='pgaTourStats', collection='summary2018')

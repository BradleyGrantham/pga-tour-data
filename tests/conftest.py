import os
import json

import pytest


@pytest.fixture()
def root_dir():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def example_stat_json(root_dir):
    filepath = os.path.join(root_dir, 'tests/test_data/test_2018stat.json')
    with open(filepath) as f:
        data = json.load(f)
        player_data = data['plrs'][0]
    return player_data

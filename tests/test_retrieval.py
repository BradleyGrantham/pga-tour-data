import pytest

from src.main import get_player_stats, get_player_ids


def test_get_player_stats(example_stat_json):
    actual = get_player_stats(28237, 2018)
    assert actual == example_stat_json


def test_valid_ids():
    player_ids = get_player_ids()
    assert all(len(id_) == 5 and isinstance(id_, str) for id_ in player_ids)

import pandas as pd
from sqlalchemy.orm import sessionmaker

from pga_tour_data.db.declarative import engine, Base, Players, SummaryStats


def _get_session():
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()


def query_pandas(query):
    return pd.read_sql(query, con=engine)


def add_players(players, merge=False):
    session = _get_session()

    if isinstance(players, dict):
        players = [players]

    if not isinstance(players, list):
        assert False, "You must pass a list of player dictionaries of just a " \
                      "single player dictionary"

    if not merge:
        f = session.add
    else:
        f = session.merge

    for player_dict in players:
        assert set(player_dict.keys()) == {'player_id',
                                           'first_name', 'last_name'}
        f(Players(**player_dict))

    session.commit()
    session.close()


def add_summary_stats(summary_stats, merge=False):
    session = _get_session()

    if isinstance(summary_stats, dict):
        summary_stats = [summary_stats]

    if not isinstance(summary_stats, list):
        assert False, "You must pass a list of player dictionaries of just a " \
                      "single player dictionary"

    if not merge:
        f = session.add
    else:
        f = session.merge

    for summary_stat_dict in summary_stats:
        assert set(summary_stat_dict.keys()) == {'player_id', 'stats'}
        f(SummaryStats(**summary_stat_dict))

    session.commit()
    session.close()


if __name__ == "__main__":
    add_players({'player_id': 99999999,
                'first_name': 'Bradley',
                'last_name': 'Grantham'})

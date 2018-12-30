import pandas as pd
from sqlalchemy.orm import sessionmaker

from pga_tour_data.db.declarative import engine, Base, Players, PlayerStats, StatNames, SummaryStats, Tournaments


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
                                           'first_name',
                                           'last_name',
                                           'nationality',
                                           'years_on_tour'}
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


def add_player_stats(stats, merge=False):
    session = _get_session()

    if isinstance(stats, dict):
        stats = [stats]

    if not isinstance(stats, list):
        assert False, "You must pass a list of player dictionaries of just a " \
                      "single player dictionary"

    if not merge:
        f = session.add
    else:
        f = session.merge

    for stat_dict in stats:
        assert set(stat_dict.keys()) == {'player_id', 'stats'}
        f(PlayerStats(**stat_dict))

    session.commit()
    session.close()


def add_stat_names(stats, merge=False):
    session = _get_session()

    if isinstance(stats, dict):
        stats = [stats]

    if not isinstance(stats, list):
        assert False, "You must pass a list of player dictionaries of just a " \
                      "single player dictionary"

    if not merge:
        f = session.add
    else:
        f = session.merge

    for stat_dict in stats:
        assert set(stat_dict.keys()) == {'stat_id', 'stat_name'}
        f(StatNames(**stat_dict))

    session.commit()
    session.close()


def add_tournaments(tournaments, merge=False):
    session = _get_session()

    if isinstance(tournaments, dict):
        tournaments = [tournaments]

    if not isinstance(tournaments, list):
        assert False, "You must pass a list of player dictionaries of just a " \
                      "single player dictionary"

    if not merge:
        f = session.add
    else:
        f = session.merge

    for tournament_dict in tournaments:
        assert set(tournament_dict.keys()) == {'tournament_year_id',
                                               'tournament_id',
                                               'year',
                                               'start_date',
                                               'end_date',
                                               'tournament_name',
                                               'course_id',
                                               'course_name',
                                               'country',
                                               'state',
                                               'city',
                                               'purse',
                                               'major'}
        f(Tournaments(**tournament_dict))

    session.commit()
    session.close()



if __name__ == "__main__":
    add_players({'player_id': 99999999,
                'first_name': 'Bradley',
                'last_name': 'Grantham'})

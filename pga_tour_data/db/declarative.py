from sqlalchemy import create_engine, Boolean, Column, DateTime, Integer, JSON, String
from sqlalchemy.ext.declarative import declarative_base

import pga_tour_data.credentials as credentials


engine = create_engine(credentials.db_engine_string)
Base = declarative_base(bind=engine)


class Players(Base):
    __tablename__ = "players"
    player_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String, nullable=False)
    nationality = Column(String)
    years_on_tour = Column(JSON)


class SummaryStats(Base):
    __tablename__ = "summary_stats"
    player_id = Column(Integer, primary_key=True)
    stats = Column(JSON)


class Tournaments(Base):
    __tablename__ = "tournaments"
    tournament_year_id = Column(String, primary_key=True)
    tournament_id = Column(String)
    year = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    tournament_name = Column(String)
    course_id = Column(String)
    course_name = Column(String)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    purse = Column(Integer)
    major = Column(Boolean)


if __name__ == "__main__":
    Base.metadata.create_all()

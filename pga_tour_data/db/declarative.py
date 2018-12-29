from sqlalchemy import create_engine, Column, Integer, JSON, String
from sqlalchemy.ext.declarative import declarative_base

import pga_tour_data.credentials as credentials


engine = create_engine(credentials.db_engine_string)
Base = declarative_base(bind=engine)


class Players(Base):
    __tablename__ = "players"
    player_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String, nullable=False)


class SummaryStats(Base):
    __tablename__ = "summary_stats"
    player_id = Column(Integer, primary_key=True)
    stats = Column(JSON)


if __name__ == "__main__":
    Base.metadata.create_all()

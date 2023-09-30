from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import decorative_base, relationship

eng = create_engine('sqlite:///movies.db')
Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key = True, autoincrement= True)
    title = Column(String(80), nullable = False)
    rating = Column(Integer, nullable = False)
    release_year = Column(String(4), nullable = False)

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key = True, autoincrement= True)
    title = Column(String(80), nullable = False)
    rating = Column(Integer, nullable = False)
    release_year = Column(String(4), nullable = False)
    amount_of_seasons = Column(Integer, nullable = False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, autoincrement= True)
    name = Column(String(20), nullable = False)
    surname = Column(String(20), default = "")

class WatchingList(Base):
    __tablename__ = 'watching_list'
    id = Column(Integer, primary_key = True, autoincrement= True)
    name = Column(String(20), nullable= False)
    date_when_created = Column(String(20), nullable=False)

if __name__ == "__main__":
    Base.metadata.create_all(eng)
    
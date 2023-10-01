from sqlalchemy.orm import sessionmaker
from models import eng, Movie, Series, User, WatchingList

Session = sessionmaker(bing=eng)
Session = Session()


def create_movie(title, rating, release_year):
    session.add(Movie(title=title, rating=rating, release_year=release_year))
    session.commit()


if __name__ == "__main__":
    create_movie('The Godfather', 9, '1972')
    

"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app
from datetime import datetime

DB_URI = "sqlite:///ratings.db"


def load_users():
    """u.user textfile | Load users from u.user into database."""
    openfile = open('./seed_data/u.user')

    for line in openfile:
        user_row = line.rstrip().split("|")
        user_stuff = User(user_id=user_row[0], age=user_row[1], zipcode=user_row[4])
        db.session.add(user_stuff)
    db.session.commit()

def load_movies():
    """u.item | Load movies from u.item into database. '01-Jan-1947'"""
    openfile = open('./seed_data/u.item')

    for line in openfile:
        movie_row = line.rstrip().split("|")
        # print movie_row
        # break
        movie_title_list = movie_row[1].split(" ")
        minus_final_value = movie_title_list[0:-1]
        final_movie_title_list = ' '.join(minus_final_value)

        s = movie_row[2]
        if s:
            released_at = datetime.strptime(s, "%d-%b-%Y")
        else:
            released_at = None 

        movie_id=movie_row[0]
        title=final_movie_title_list
        released_at=released_at
        imdb_url=movie_row[4]

        movie_stuff = Movie(movie_id=movie_id, title=title, released_at=released_at, imdb_url=imdb_url)
        db.session.add(movie_stuff)
    db.session.commit()

  

def load_ratings():
    """u.data \ t Load ratings from u.data into database.user_id \ t movie_id \ t score \ t timestamp.

    """

    openfile = open('./seed_data/u.data')

    for line in openfile:
        rating_row = line.rstrip().split("\t")
        rating_stuff = Rating(user_id=rating_row[0], movie_id=rating_row[1], score=rating_row[2])        
        db.session.add(rating_stuff)
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    load_movies()
    load_ratings()

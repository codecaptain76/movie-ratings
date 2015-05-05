"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app

DB_URI = "sqlite:///ratings.db"


def load_users():
    """u.user textfile | Load users from u.user into database."""
    openfile = open('./seed_data/u.user')

    for line in openfile:
        user_row = line.rstrip().split("|")
        user_stuff = User(user_id=user_row[0], age=user_row[1], zipcode=user_row[2])
        print user_row
        print user_stuff
        db.session.add(user_row)
        db.commit()

def load_movies():
    """u.item | Load movies from u.item into database."""
    openfile = open('./seed_data/u.item')

    for line in openfile:
        movie_id = line.split("|")
        released_at = datetime.strptime()
        db.session.add(movie_id)
        db.session.add(released_at)
        db.commit()

def load_ratings():
    """u.data \ t Load ratings from u.data into database."""

    openfile = open('./seed_data/u.data')

    for line in openfile:
        rating_id = line.split("/t")
        db.session.add(rating_id)
        db.commit()

if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    load_movies()
    load_ratings()

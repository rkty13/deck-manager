from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from application import app
from application import models

def create_deck(title, user_id):
    engine = create_engine(app.config["DB"])
    Session = sessionmaker(bind = engine)
    session = Session()

    def create_helper():
        new_deck = models.decks.DeckMeta(title, user_id)
        return new_deck

    new_deck = create_helper()

    try:
        session.add(new_deck)
        session.commit()
    except OperationalError:
        models.create_db(engine)
        session.add(new_deck)
        session.commit()

    session.close()
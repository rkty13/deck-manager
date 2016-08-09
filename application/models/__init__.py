from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from application import app

Base = declarative_base()

def create_db(engine):
    Base.metadata.create_all(engine)

from . import cards
from . import decks
from . import users

engine = create_engine(app.config["DB"])
create_db(engine)
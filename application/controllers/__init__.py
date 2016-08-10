from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application import app

engine = create_engine(app.config["DB"])
session_object = sessionmaker(bind = engine)

from . import users
from . import decks
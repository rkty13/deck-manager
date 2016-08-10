from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from application import app
from application import models

def create_user(username, email, password):
    engine = create_engine(app.config["DB"])
    Session = sessionmaker(bind = engine)
    session = Session()

    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    new_user = models.users.Users(username, email, hashed)

    try:
        session.add(new_user)
        session.commit(new_user)
    except OperationalError:
        models.create_db(engine)
        session.add(new_user)
        session.commit(new_user)
    session.close()

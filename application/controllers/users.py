from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from . import engine

from application import app
from application import models


def create_user(username, email, password, session_object):
    session = session_object()

    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    new_user = models.users.Users(username, email, hashed)

    try:
        session.add(new_user)
        session.commit()
    except OperationalError:
        models.create_db(engine)
        session.add(new_user)
        session.commit()
    finally:
        session.close()

def get_user(id, session_object):
    session = session_object()

    def query_helper():
        try:
            user = session.query(models.users.Users).filter(models.users.Users.id == id).one()
            if user is not None:
                return user
        except NoResultFound:
            return None
        except MultipleResultsFound:
            return None

    try:
        return query_helper()
    except OperationalError:
        models.create_db(engine)
        return query_helper()
    finally:
        session.close()

def delete_user(id, session_object):
    session = session_object()

    user = get_user(id, session_object)
    if user == None:
        print("Error: User does not exist")
        return
    else:
        try:
            session.delete(user)
            session.commit()
        except OperationalError:
            print("Error: Something is wrong")
        finally:
            session.close()

def save_user(id, username, email, password, session_object):
    session = session_object()
    user = get_user(id, session_object)
    if user == None:
        print("Error: User does not exist")
        return
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    else:
        try:
            user.username = username
            user.email = email
            user.password = hashed
            session.commit()
        except OperationalError:
            models.create_db(engine)
            user.username = username
            user.email = email
            user.password = hashed
            session.commit()
        finally:
            session.close()

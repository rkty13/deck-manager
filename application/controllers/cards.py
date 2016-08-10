from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from . import engine

from application import app
from application import models

def get_card(title, type, attack, defense, attribute, sub_type, desc, printing_code, level, pendulum_scale, pendulum_effect, password, session_object):
    session = session_object()

    search_attributes = {}

    if title is not None:
        search_attributes['title'] = title

    if type is not None:
        search_attributes['type'] = type

    if attack is not None:
        search_attributes['attack'] = attack

    if defense is not None:
        search_attributes['defense'] = defense

    if attribute is not None:
        search_attributes['attribute'] = attribute

    if sub_type is not None:
        search_attributes['sub_type'] = sub_type

    if desc is not None:
        search_attributes['desc'] = desc

    if printing_code is not None:
        search_attributes['printing_code'] = printing_code

    if level is not None:
        search_attributes['level'] = level

    if pendulum_scale is not None:
        search_attributes['pendulum_scale'] = pendulum_scale

    if pendulum_effect is not None:
        search_attributes['pendulum_effect'] = pendulum_effect

    if password is not None:
        search_attributes['password'] = password

    def get_card_helper():
        card = session.query(models.cards.Cards).filter(**search_attributes)
        if card is not None:
            return card

    try:
        return get_card_helper()
    except NoResultFound:
        return None
    except MultipleResultsFound:
        return None
    except OperationalError:
        models.create_db(engine)
        return get_card_helper()
    finally:
        session.close()

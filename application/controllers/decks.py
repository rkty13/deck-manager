from sqlalchemy import and_
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from . import engine

from application import app
from application import models

def create_deck(title, user_id, session_object):
    session = session_object()

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
    finally:
        session.close()

def get_deck_meta(deck_meta_id, session_object):
    session = session_object()

    def get_meta_helper():
        deck_meta = session.query(models.decks.DeckMeta) \
            .filter(models.decks.DeckMeta.id == deck_meta_id).one()

        if deck_meta is not None:
            return deck_meta

    try:
        return get_meta_helper()
    except NoResultFound:
        return None
    except OperationalError:
        models.create_db(engine)
        return get_meta_helper()
    except MultipleResultsFound:
        return None
    finally:
        session.close()

def get_deck(deck_meta_id, session_object):
    session = session_object()

    def get_deck_helper():
        deck = session.query(models.decks.DeckMeta, models.decks.DeckCards) \
            .filter(models.decks.DeckMeta.id == deck_meta_id) \
            .join("deck_cards").all()
        return deck

    try:
        return get_deck_helper()
    except OperationalError:
        models.create_db(engine)
        return get_deck_helper()
    finally:
        session.close()

def get_card_in_deck(deck_meta_id, card_id, session_object):
    session = session_object()

    def get_card_helper():
        card = session.query(models.decks.DeckCards) \
            .filter(and_(models.decks.DeckCards.card_id == card_id, 
                            models.decks.DeckCards.deck_id == deck_meta_id)).one()
        return card

    try:
        return get_card_helper()
    except OperationalError:
        models.create_db(engine)
        return get_card_helper()
    except MultipleResultsFound:
        return None
    except NoResultFound:
        return None
    finally:
        session.close()

def add_card_to_deck(deck_meta_id, card_id, deck_type, session_object):
    session = session_object()

    def add_card_helper():
        card = get_card_in_deck(deck_meta_id, card_id, session_object)
        if card is not None:
            card.quantity += 1
            return card
        else:
            new_card = models.decks.DeckCards(deck_meta_id, card_id, 1, deck_type)
            return new_card

    card = add_card_helper()
    
    try:
        session.add(card)
        session.commit()
    except OperationalError:
        models.create_db(engine)
        session.add(card)
        session.commit()
    finally:
        session.close()


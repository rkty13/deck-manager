from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from . import Base

class DeckMeta(Base):
    __tablename__ = "DeckMeta"
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(255))
    user_id = Column(Integer, ForeignKey("Users.id"))
    date_created = Column(DateTime)
    deck_cards = relationship("DeckCards", backref = "DeckMeta.id")

    def __init__(self, title, user_id, date_created):
        self.title = title
        self.user_id = user_id
        self.date_created = date_created


class DeckCards(Base):
    __tablename__ = "DeckCards"
    id = Column(Integer, primary_key = True, autoincrement = True)
    deck_id = Column(Integer, ForeignKey("DeckMeta.id"))
    card_id = Column(Integer, ForeignKey("Cards.id"))
    quantity = Column(Integer)
    deck_type = Column(String(255))

    def __init__(self, deck_id, card_id, quantity, deck_type):
        self.deck_id = deck_id
        self.card_id = card_id
        self.quantity = quantity
        self.deck_type = deck_type
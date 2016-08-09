from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DeckMeta(Base):
    __tablename__ = "DeckMeta"
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(255))
    created_by = Column(String(255))
    date_created = Column(DateTime)
    deck_cards = relationship("DeckCards")

    def __init__(self, title, created_by, date_created):
        self.title = title
        self.created_by = created_by
        self.date_created = date_created


class DeckCards(Base):
    __tablename__ = "DeckCards"
    id = Column(Integer, primary_key = True, autoincrement = True)
    deck_id = Column(Integer, ForeignKey("DeckMeta.id"))
    card_id = Column(Integer, ForeignKey("Card.id"))
    quantity = Column(Integer)
    deck_type = Column(String(255))

    def __init__(self, deck_id, card_id, quantity, deck_type):
        self.deck_id = deck_id
        self.card_id = card_id
        self.quantity = quantity
        self.deck_type = deck_type

        
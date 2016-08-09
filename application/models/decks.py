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



    def __init__(self):
        

class DeckCards(Base):
    __tablename__ = "DeckCards"
    id = Column(Integer, primary_key = True, autoincrement = True)
    deck_id = Column(Integer, ForeignKey("DeckMeta.id"))

    def __init__(self):
        self.title = title 
        self.type = type 
        self.attack = attack 
        self.defense = defense 
        self.attribute = attribute 
        self.sub_type = sub_type 
        self.desc = desc 
        self.printing_code = printing_code 
        self.level = level 
        self.pendulum_scale = pendulum_scale 
        self.pendulum_effect = pendulum_effect 
        self.password = password 
        self.image_url = image_url 
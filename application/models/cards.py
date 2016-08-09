from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Card(Base):
    __tablename__ = "Cards"
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(Text)
    type = Column(Text)
    attack = Column(Integer)
    defense = Column(Integer)
    attribute = Column(Text)
    sub_type = Column(Text)
    desc = Column(Text)
    printing_code = Column(Text)
    level = Column(Integer)
    pendulum_scale = Column(Integer)
    pendulum_effect = Column(Text)
    password = Column(Text)
    image_url = Column(Text)

    def __init__(self, title, type, attack, defense, attribute, sub_type, desc, printing_code, level, pendulum_scale, pendulum_effect, password, image_url):
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

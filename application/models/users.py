from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True, autoincrement = True)
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    premium = Column(Boolean, default = False, nullable = False)
    date_created = Column(DateTime)
    deck_meta = relationship("DeckMeta", backref = "Users.id")

    def __init__(self, username, email, password, date_created):
        self.username = username
        self.email = email
        self.password = password
        self.date_created = date_created

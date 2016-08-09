from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key = True, autoincrement = True)
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    premium = Column(Boolean, default = False)
    date_created = Column(DateTime)

    def __init__(self):

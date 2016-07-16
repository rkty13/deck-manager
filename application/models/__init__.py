from . import cards

def create_db(engine):
    cards.Base.metadata.create_all(engine)
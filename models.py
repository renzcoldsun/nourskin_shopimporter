from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from config import connection_string

engine = create_engine(connection_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Item(Base):
    __tablename__ = 'payout_item'
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    description = Column(String)
    sale_price = Column(Float)
    dealer_price = Column(Float)

    def getItems(self):
        items = [];
        for item in session.query(Item):
            items.append(item)
        return items

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from config import connection_string
from woocommerce import API as wooo_api

engine = create_engine(connection_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

api_consumer_key = "ck_f65e9c5b696f93404da8cf79fdfd98fe5da293cc"
api_consumer_secret = "cs_92a2c541f735b0ac90000875194b6a961321b462"

wcapi = wooo_api(
                url="http://localhost",
                consumer_key = api_consumer_key,
                consumer_secret = api_consumer_secret,
                version = "wc/v3"
                )

class Item(Base):
    __tablename__ = 'payout_item'
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    description = Column(String)
    sale_price = Column(Float)
    dealer_price = Column(Float)

for item in session.query(Item):
    product_link = "products/" + str(item.id)
    woo_item = wcapi.get(product_link)
    if woo_item.status_code == 404:
        print("INSERT")
    else:
        print("UPDATE")


from sqlalchemy import Column, Integer, String

from .base import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    buy_price = Column(Float, default=0.0)
    sell_price = Column(Float, default=0.0)
    stock = Column(Integer, default=0)
    bar_codes = Column(Text)
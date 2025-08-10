from sqlalchemy import Column, Integer, ForeignKey, Float

from .base import Base

class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, default=1)
    price = Column(Float, default=0.0)
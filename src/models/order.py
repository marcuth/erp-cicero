from sqlalchemy import Column, Integer, Float, Enum, DateTime

from enums.payment_type import PaymentType
from utils.utc_now import utc_now
from .base import Base

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True)
    seller_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    total_price = Column(Float, default=0)
    payment_type = Column(Enum(PaymentType), nullable=False)
    created_at = Column(DateTime, default=utc_now)
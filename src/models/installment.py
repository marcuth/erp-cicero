from sqlalchemy import Column, Integer, DateTime, Date, Float, String

from .base import Base

class Installment(Base):
    __tablename__ = "installments"
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    seller_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    must_be_paid_at = Column(Date, nullable=False)
    paid_at = Column(DateTime, nullable=True)
    received_by_seller_id = Column(Integer, nullable=True)
    amount = Column(Float, default=0.0)
    status = Column(String(20), default="PENDING")
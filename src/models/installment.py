from sqlalchemy import Column, Integer, DateTime, Date, Float, Enum

from enums.installment_status import InstallmentStatus
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
    status = Column(Enum(InstallmentStatus), nullable=False, default=InstallmentStatus.PENDING)
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, ForeignKey, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DB_FILE = "erp_data.db"
DB_URL = f"sqlite:///{DB_FILE}"

from .base import Base
engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)





class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True)
    seller_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    total_price = Column(Float, default=0.0)
    payment_type = Column(String(30))
    created_at = Column(DateTime, default=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, default=1)
    price = Column(Float, default=0.0)

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
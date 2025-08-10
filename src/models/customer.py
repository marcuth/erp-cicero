from sqlalchemy import Column, Integer, String, Boolean

from .base import Base

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cpf = Column(String(30), nullable=False)
    state = Column(String(80), nullable=False)
    city = Column(String(120), nullable=False)
    address = Column(String(250), nullable=False)
    phone = Column(String(80), nullable=False)
    email = Column(String(150), nullable=False)
    gender = Column(Boolean, nullable=False)

from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    name = Column(String(250))
    role = Column(String(20))
    password_hash = Column(String(256))
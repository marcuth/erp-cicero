
from sqlalchemy import Column, Integer, String, Enum

from enums.user_role import UserRole
from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    name = Column(String(250))
    role = Column(Enum(UserRole), nullable=False)
    password = Column(String(256))
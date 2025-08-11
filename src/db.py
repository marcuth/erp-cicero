from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from models import Base, BarCode, Customer, Order, OrderItem, User
from config import DB_URL

engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
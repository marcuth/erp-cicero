from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, ForeignKey, Date
from sqlalchemy.orm import sessionmaker

from utils.utc_now import utc_now

DB_FILE = "erp_data.db"
DB_URL = f"sqlite:///{DB_FILE}"

from .base import Base
engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)






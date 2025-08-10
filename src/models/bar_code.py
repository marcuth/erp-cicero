from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class BarCode(Base):
    __tablename__ = "product_barcodes"
    id = Column(Integer, primary_key=True)
    code = Column(String(50), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))

    product = relationship("Product", back_populates="bar_codes")
from .base import Base
from sqlalchemy import Boolean, Column, String

class Currency(Base):
    __tablename__ = 'currencies'

    name: str = Column(String) 
    symbol: str = Column(String, primary_key=True)
    enabled: bool = Column(Boolean)


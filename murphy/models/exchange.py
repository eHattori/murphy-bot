from sqlalchemy import Column, String, Integer
from .base import Base

class Exchange(Base):
    __tablename__ = 'exchanges'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)


from .base import Base
from .exchange import Exchange
from .currency import Currency
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Dataset(Base):
    __tablename__ = 'datasets'

    pair: str = Column(String, primary_key=True)
    period_start: str = Column(String)
    period_end: str = Column(String)
    currency: str = Column(String)
    asset: str = Column(String)
    
    exchange_id: int = Column(Integer, ForeignKey("exchanges.id"))
    exchange: Exchange =  relationship("Exchange")

    currency_id: str = Column(String, ForeignKey("currencies.symbol"))
    currency: Currency = relationship("Currency")



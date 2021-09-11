from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base
from .dataset import Dataset
from .exchange import Exchange
from .currency import Currency

class Price(Base):
    __tablename__ = 'prices'

    pair: str = Column(String, primary_key=True) 
    current: float = Column(Float, default=0)
    lowest: float = Column(Float, default=0)
    highest: float = Column(Float, default=0)
    volume: float = Column(Float, default=0)
    asset: str = Column(String)
    openAt: str = Column(String)

    dataset_id: str = Column(String, ForeignKey("datasets.pair"))
    dataset: Dataset =  relationship("Dataset")

    exchange_id: int = Column(Integer, ForeignKey("exchanges.id"))
    exchange: Exchange = relationship("Exchange")

    currency_id: str = Column(String, ForeignKey("currency.symbol"))
    currency: Currency = relationship("Currency")

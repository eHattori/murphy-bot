from sqlalchemy import Column, Boolean, String, Integer, Float
from .base import Base

class Order(Base):
    BUY = 'BUY'
    SELL = 'SELL'

    TYPE_LIMIT = 'LIMIT'
    TYPE_MARKET = 'MARKET'
    TYPE_STOP_LOSS = 'STOP_LOSS'
    TYPE_STOP_LOSS_LIMIT = 'STOP_LOSS_LIMIT'
    TYPE_TAKE_PROFIT = 'TAKE_PROFIT'
    TYPE_TAKE_PROFIT_LIMIT = 'TAKE_PROFIT_LIMIT'
    TYPE_LIMIT_MAKER = 'LIMIT_MAKER'

    __tablename__ = 'orders'

    type: str = Column(String, default=TYPE_LIMIT)
    symbol: str = Column(String, primary_key=True)
    currency: str = Column(String)
    asset: str = Column(String)
    price: float = Column(Float)
    quantity: int = Column(Integer)
    test: bool = Column(Boolean, default=False)


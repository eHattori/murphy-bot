import sys
from datetime import datetime

from datetime import datetime

from database import Database
from exchanges.exchange import Exchange
from models.dataset import Dataset
from models.price import Price
from models.currency import Currency
from models.base import Base
from config import settings

class Backtest:
    def __init__(self, exchange: Exchange,  start_date: datetime = None, end_date: datetime = None, interval:
            int = 60):

        end_date = end_date or datetime.now()
        db = Database()
        Base.metadata.create_all(db.engine)

        coin = Currency()
        coin.symbol = 'BTC'
        coin.name = 'Bitcoin'
        coin.enabled = True
        coin.save()

        exchange.set_currency(coin.symbol) 
        exchange.strategy.start()


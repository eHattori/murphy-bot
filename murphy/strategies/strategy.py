import threading
import time
from datetime import datetime
from abc import ABC, abstractmethod

from models.order import Order
from models.price import Price


class Strategy(ABC):
    TRADING_MODE_TEST = 'test'
    TRADING_MODE_REAL = 'real'

    price: Price

    def __init__(self, exchange, interval=60, *args, **kwargs):
        self.exchange = exchange
        self._timer = None
        self.interval = interval
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()
        self.portfolio = {}
        self.test = True
        self.balance = 0

    def _run(self):
        self.is_running = False
        self.start()
        self.set_price(self.exchange.symbol_ticker())
        self.run()

    @abstractmethod
    def run(self):
        pass


    def start_backtest(self, period_start, period_end, interval):
        prices = self.exchange.historical_symbol_ticker_candle(period_start, period_end)
        
        firt_price = float(prices[0].current)
        self.balance = self.balance / firt_price
        first_balance = self.balance

        for price in prices:
            self.set_price(price)
            self.run()

        print('START With: ', first_balance)
        print('ENDED With: ', self.balance if self.balance else self.current_position)

    def start(self):
        if not self.is_running:
            print(datetime.now())
            if self._timer is None:
                self.next_call = time.time()
            else:
                self.next_call += self.interval

            self._timer = threading.Timer(self.next_call - time.time(), self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

    def get_portfolio(self):
        self.portfolio = {'currency': self.exchange.get_asset_balance(self.exchange.currency),
                'asset': self.exchange.get_asset_balance(self.exchange.asset)}

        def get_price(self):
            return self.price

    def set_price(self, price: Price):
        self.price = price

    def buy(self, **kwargs):
        order = Order(
                currency=self.exchange.currency,
                asset=self.exchange.asset,
                symbol=self.exchange.get_symbol(),
                type=Order.TYPE_LIMIT,
                side=Order.BUY,
                test=self.test,
                **kwargs
                )
        self.order(order)

    def sell(self, **kwargs):
        order = Order(
                currency=self.exchange.currency,
                asset=self.exchange.asset,
                symbol=self.exchange.get_symbol(),
                side=Order.SELL,
                test=self.test,
                **kwargs
                )
        self.order(order)

    def order(self, order: Order):
        print(order)
        exchange_order = self.exchange.order(order)


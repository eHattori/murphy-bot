from config import settings

from exchanges.mock_binance import MockBinance
from strategies.default_strategy import DefaultStrategy
from database import Database
from services.backtest import Backtest


exchange = None
def main():
    Database.build()
    exchange = MockBinance(key=settings.api_key, secret=settings.api_secret)

    print("Connecting to {} exchange...".format(exchange.name.upper()))

    exchange.set_currency(settings.currency)
    exchange.set_asset(settings.asset)

    exchange.set_strategy(DefaultStrategy(exchange=exchange))
    print("{} mode on {} symbol".format('live', exchange.get_symbol()))

    period_start = '2021-09-01T08:49' 
    period_end = '2021-09-11T08:49'
    interval = settings.candle_interval 
    print(
        "Backtest period from {} to {} with {} seconds candlesticks.".format(
            period_start,
            period_end,
            interval
        )
    )
    Backtest(exchange, period_start, period_end, interval)


def stop(*args):
    if (exchange.socket):
        print('Closing WebSocket connection...')
        exchange.close_socket()
        sys.exit(0)
    else:
        print('stopping strategy...')
        exchange.strategy.stop()
        exchange.strategy.stop()


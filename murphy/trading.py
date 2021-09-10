from .config import Config

from .exchanges.binance import Binance
from murphy.strategies.watcher import Watcher

from .services.backtest import Backtest


exchange = None
def main():
    config = Config()
    exchange = Binance(key=config.BINANCE_API_KEY, secret=config.BINANCE_API_SECRET)

    print("Connecting to {} exchange...".format(exchange.name.upper()))

    exchange.set_currency(config.CURRENCY)
    exchange.set_asset(config.ASSET)

    exchange.set_strategy(Watcher(exchange=exchange))

    print("{} mode on {} symbol".format('live', exchange.get_symbol()))
    exchange.strategy.start()
    # if mode == 'trade':
    #     exchange.strategy.start()
    
    # elif mode == 'live':
    # exchange.start_symbol_ticker_socket(exchange.get_symbol())
    
    # elif mode == 'backtest':
    # period_start = config.get('PERIOD_START')
    # period_end = config.get('PERIOD_END')
    # interval = config.get('CANDLE_INTERVAL') 
    # print(
    #     "Backtest period from {} to {} with {} seconds candlesticks.".format(
    #         period_start,
    #         period_end,
    #         interval
    #     )
    # )
    # Backtest(exchange, period_start, period_end, interval)


def stop(*args):
    if (exchange.socket):
        print('Closing WebSocket connection...')
        exchange.close_socket()
        sys.exit(0)
    else:
        print('stopping strategy...')
        exchange.strategy.stop()
        exchange.strategy.stop()


from configparser import ConfigParser
import os

class Config:
    CFG_FL_NAME = "user.cfg"

    def __init__(self):
        config = ConfigParser(allow_no_value=True)
        config.optionxform = str
        config['DEFAULT'] = {
                'tld': 'com',
                'currency': 'BTC',
                'asset': 'USDT',
                'candle_interval': 60,
                'api_key': None,
                'api_secret': None,
                'exchange': 'binance',
                'database_url': 'sqlite:///data/crypto_trading.db'
                }

        if os.path.exists(self.CFG_FL_NAME):
            config.read(self.CFG_FL_NAME, encoding='utf-8-sig')

        self.__dict__.update(config.items('DEFAULT'))

settings = Config()

from configparser import ConfigParser
import os

CFG_FL_NAME = "user.cfg"
BINANCE_CFG_SECTION = "binance_user_config"

config = ConfigParser()
class Config:

    def __init__(self):
        config['DEFAULT'] = {
                'tld': 'com',
                'currency': 'BTC',
                'asset': 'USDT',
                'PERIOD_START': '2021-02-28T08:49',
                'PERIOD_END':'2021-03-09T08:49',
                'CANDLE_INTERVAL': 60,
                'API_ROOT': 'http://localhost/',
                'API_URI': 'api/',
                'API_ENDPOINT_PRICE': 'http://localhost/api/prices'
                }

        if os.path.exists(CFG_FL_NAME):
            config.read(CFG_FL_NAME)

        self.BINANCE_API_KEY = os.environ.get('BINANCE_API_KEY',
                config.get(BINANCE_CFG_SECTION, 'api_key'))

        self.BINANCE_API_SECRET = os.environ.get('BINANCE_SECRET_KEY',
                config.get(BINANCE_CFG_SECTION, 'api_secret_key'))

        self.BINANCE_TLD = os.environ.get('BINANCE_TLD',
                config.get(BINANCE_CFG_SECTION, 'tld'))

        self.CURRENCY = os.environ.get('CURRENCY', config.get('DEFAULT', 'currency'))
        self.ASSET = os.environ.get('ASSET', config.get('DEFAULT', 'asset'))


    @staticmethod
    def get(key, schema='DEFAULT'):
        return config.get(schema, key)


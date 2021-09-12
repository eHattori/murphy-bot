from sqlalchemy import create_engine

from config import settings


class Database:

    _instance = None

    def __init__(self):
        self.engine = create_engine(settings.database_url)
    
    @classmethod
    def build(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


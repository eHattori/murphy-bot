from sqlalchemy import create_engine

from config import settings


class Database:

    def __init__(self):
        self.engine = create_engine(settings.database_url)



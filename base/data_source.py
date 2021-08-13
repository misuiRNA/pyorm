from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DataSource:

    def __init__(self, db_url):
        self._engine = create_engine(db_url)
        self._engine.connect()
        self._session = sessionmaker(bind=self._engine)()

    @property
    def session(self):
        return self._session



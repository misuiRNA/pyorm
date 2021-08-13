
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.my_session import Base


class MockDatabase:
    _engine = create_engine("sqlite:///:memory:")
    _session = sessionmaker(bind=_engine)()

    # TODO should mock 'Base' instead of import it form product environment
    # Base = declarative_base(engine)
    def __init__(self):
        Base.metadata.create_all(self._engine)

    def __del__(self):
        Base.metadata.drop_all(self._engine)

    @property
    def session(self):
        return self._session



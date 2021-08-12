import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.my_session import Base


class AbstractTest(unittest.TestCase):

    _engine = create_engine("sqlite:///:memory:")
    _session = sessionmaker(bind=_engine)()

    def setUp(self):
        Base.metadata.create_all(self._engine)

    def tearDown(self):
        Base.metadata.drop_all(self._engine)

import unittest

from test.utils.mock_database import MockDatabase


class AbstractTest(unittest.TestCase):

    def setUp(self):
        self._mock_db = MockDatabase()
        self._session = self._mock_db.session

    def tearDown(self):
        del self._mock_db

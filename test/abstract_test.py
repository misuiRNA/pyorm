import unittest

from test.utils.mock_data_source import MockDataSource


class AbstractTest(unittest.TestCase):

    def setUp(self):
        self._mock_ds = MockDataSource()
        self._session = self._mock_ds.session

    def tearDown(self):
        del self._mock_ds

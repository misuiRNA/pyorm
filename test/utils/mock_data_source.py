from base.data_source import DataSource
from base.base_table import Base


class MockDataSource(DataSource):
    _URL = "sqlite:///:memory:"

    def __init__(self):
        super().__init__(self._URL)
        Base.metadata.create_all(self._engine)

    def __del__(self):
        Base.metadata.drop_all(self._engine)

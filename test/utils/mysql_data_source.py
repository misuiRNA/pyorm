from base.data_source import DataSource


class MysqlDataSource(DataSource):
    _URL = f"mysql+pymysql://root:root@mysql:3306/contract"

    def __init__(self):
        super().__init__(self._URL)


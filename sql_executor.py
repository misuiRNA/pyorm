from config.my_session import session
from sqlalchemy.orm import Query

from dao.abstract_dao import AbstractDao


class SqlExecutor:

    def __init__(self, dao: AbstractDao):
        self._domain_class = dao.domain()
        self._ormapping = dao.ormapping()
        self._join_conf = dao.union_table()

    def query(self):
        query_pattern = []
        for attr, table_column in self._ormapping.items():
            query_pattern.append(table_column.label(attr))

        query: Query = session.query(*query_pattern)

        if self._join_conf:
            query = query.join(*self._join_conf)
        return query

    def row_with_single_table(self, domain):
        table_class = None

        kwargs = {"is_deleted": False}
        for attr in self._ormapping:
            value = getattr(domain, f"_{attr}")

            table_conf = self._ormapping[attr]
            if table_class is None:
                table_class = table_conf.class_
            elif table_class != table_conf.class_:
                raise Exception(f"domain class {self._domain_class} is not mapped with only one table !")

            column_name = self._ormapping[attr].key
            kwargs.update({
                column_name: value
            })
        row = table_class(**kwargs)
        return row

    def one(self, sql_query: Query):
        result = sql_query.first()
        entity = self._create_entity(result)
        return entity

    def list_all(self, sql_query: Query):
        result_list = sql_query.all()

        entity_list = []
        for item in result_list:
            entity = self._create_entity(item)
            entity_list.append(entity)
        return entity_list

    def count(self, sql_query: Query):
        count = sql_query.count()
        return count

    def update(self, entity):
        kwargs = {self._ormapping[attr]: getattr(entity, f"_{attr}") for attr in self._ormapping}

        # TODO try to optimize
        q = self.query().filter(self._ormapping["id"] == entity.id)
        q.update(kwargs)
        session.flush()

    def insert(self, row_list):
        session.add_all(row_list)
        session.flush()

    def _query_param(self):
        query_pattern = []
        for attr, table_column in self._ormapping.items():
            query_pattern.append(table_column.label(attr))
        return query_pattern

    def _create_entity(self, sql_result):
        inst = self._domain_class()

        for attr in self._ormapping:
            if not hasattr(sql_result, attr):
                raise Exception(f"can't find attr '{attr}' in sql query result !")
            value = getattr(sql_result, attr)
            inst.__setattr__(f"_{attr}", value)
        return inst

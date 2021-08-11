from sqlalchemy import func

from dao.abstract_dao import AbstractDao
from domain.doctype import Doctype
from sql_executor import SqlExecutor
from table.doctype_table import DocTypeTable
from table.mark_task_group_table import MarkTaskGroupTable


class DoctypeDao(AbstractDao):
    _domain = Doctype
    _ormapping = {
        "doctype_id":       DocTypeTable.id,
        "doctype_name":     DocTypeTable.name,
        "desc":             DocTypeTable.desc,
        "create_time":      DocTypeTable.create_time,
        "last_update_time": DocTypeTable.last_update_time,
        "placeholder":      MarkTaskGroupTable.doc_type_id,
        "group_count":      func.count("*")
    }
    _union_table = [MarkTaskGroupTable, MarkTaskGroupTable.doc_type_id == DocTypeTable.id]

    @classmethod
    def list_doctype(cls, start, limit_num, search, include_deleted=False):
        filter_pattern = [DocTypeTable.name.like(f"%{search}%")]
        if not include_deleted:
            filter_pattern.append(~MarkTaskGroupTable.is_deleted)

        executor = SqlExecutor(cls())
        q = executor.query() \
            .group_by(MarkTaskGroupTable.doc_type_id) \
            .filter(*filter_pattern) \
            .order_by(DocTypeTable.create_time.desc()) \
            .offset(start)\
            .limit(limit_num)

        doctype_list = executor.list_all(q)
        return doctype_list

    @classmethod
    def total_count(cls, include_deleted=False):
        filter_pattern = []
        if not include_deleted:
            filter_pattern.append(~MarkTaskGroupTable.is_deleted)

        executor = SqlExecutor(cls())
        q = executor.query() \
            .group_by(MarkTaskGroupTable.doc_type_id) \
            .filter(*filter_pattern)
        count = executor.count(q)
        return count



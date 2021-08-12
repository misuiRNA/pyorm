from typing import List

from sqlalchemy import func

from domain.doctype import Doctype
from table.doctype_table import DocTypeTable
from table.mark_task_group_table import MarkTaskGroupTable


class DoctypeDao:

    _query_entity = [
        DocTypeTable.id,
        DocTypeTable.name,
        DocTypeTable.desc,
        MarkTaskGroupTable.doc_type_id,
        func.count("*").label("group_count")

    ]

    def __init__(self, db_session):
        self._session = db_session

    def list_all(self, start, limit_num, search):
        q = self._session.query(*self._query_entity)\
         .join(MarkTaskGroupTable, MarkTaskGroupTable.doc_type_id == DocTypeTable.id)\
         .group_by(MarkTaskGroupTable.doc_type_id) \
         .filter(DocTypeTable.name.like(f"%{search}%")) \
         .offset(start)\
         .limit(limit_num)
        result_list = q.all()

        doctype_list: List[Doctype] = []
        for result in result_list:
            doctype = Doctype(
                doctype_id=result.doc_type_id,
                doctype_name=result.name,
                desc=result.desc,
                group_count=result.group_count,
            )
            doctype_list.append(doctype)
        return doctype_list

    def total_count(self):
        q = self._session.query(*self._query_entity)\
         .join(MarkTaskGroupTable, MarkTaskGroupTable.doc_type_id == DocTypeTable.id)\
         .group_by(MarkTaskGroupTable.doc_type_id)
        count = q.count()
        return count

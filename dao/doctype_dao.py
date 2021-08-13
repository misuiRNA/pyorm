from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Session

from base.ormapper import ORMapper
from domain.doctype import Doctype
from table.doctype_table import DocTypeTable
from table.mark_task_group_table import MarkTaskGroupTable


class DoctypeDao:
    _mapping = dict(
        id=DocTypeTable.id,
        name=DocTypeTable.name,
        desc=DocTypeTable.desc,
        doctype_id=MarkTaskGroupTable.doc_type_id,
        group_count=func.count("*").label("group_count")
    )
    _orm = ORMapper(Doctype, _mapping)

    def __init__(self, db_session):
        self._session: Session = db_session

    def list_all(self, start, limit_num, search):
        q = self._session.query(*self._orm.query_entity())\
         .join(MarkTaskGroupTable, MarkTaskGroupTable.doc_type_id == DocTypeTable.id)\
         .group_by(MarkTaskGroupTable.doc_type_id) \
         .filter(DocTypeTable.name.like(f"%{search}%")) \
         .offset(start)\
         .limit(limit_num)
        result_list = q.all()

        doctype_list: List[Doctype] = []
        for result in result_list:
            doctype = self._orm.parse(result)
            doctype_list.append(doctype)
        return doctype_list

    def total_count(self):
        q = self._session.query(*self._orm.query_entity())\
         .join(MarkTaskGroupTable, MarkTaskGroupTable.doc_type_id == DocTypeTable.id)\
         .group_by(MarkTaskGroupTable.doc_type_id)
        count = q.count()
        return count

from typing import List

from sqlalchemy import func

from config.my_session import session
from domain.doctype import Doctype
from table.doctype_table import DocTypeTable
from table.mark_task_group_table import MarkTaskGroupTable


class DoctypeDao:

    @classmethod
    def list_all(cls, start, limit_num, search):
        q = session.query(
            DocTypeTable.id,
            DocTypeTable.name,
            DocTypeTable.desc,
            DocTypeTable.create_time,
            DocTypeTable.last_update_time,
            MarkTaskGroupTable.doc_type_id,
            func.count("*").label("group_count")
        ).join(MarkTaskGroupTable, MarkTaskGroupTable.doc_type_id == DocTypeTable.id)\
         .group_by(MarkTaskGroupTable.doc_type_id) \
         .filter(DocTypeTable.name.like(f"%{search}%")) \
         .order_by(DocTypeTable.create_time.desc()) \
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
                create_time=result.create_time,
                last_update_time=result.last_update_time
            )
            doctype_list.append(doctype)
        return doctype_list

    @classmethod
    def total_count(cls):
        q = session.query(
            DocTypeTable.id,
            DocTypeTable.name,
            DocTypeTable.desc,
            DocTypeTable.create_time,
            DocTypeTable.last_update_time,
            MarkTaskGroupTable.doc_type_id,
            func.count("*").label("group_count")
        ).join(MarkTaskGroupTable, MarkTaskGroupTable.doc_type_id == DocTypeTable.id)\
         .group_by(MarkTaskGroupTable.doc_type_id)
        count = q.count()
        return count

from typing import List

from sqlalchemy.orm import Session

from base.ormapper import ORMapper
from dao.template_dao import TemplateDao
from domain.mark_task import MarkTask
from table.mark_task_table import MarkTaskTable


class MarkTaskDao:
    _mapping = dict(
        id=MarkTaskTable.id,
        group_id=MarkTaskTable.group_id,
        mark_data=MarkTaskTable.mark_task_result
    )
    _orm = ORMapper(MarkTask, _mapping)

    def __init__(self, db_session):
        self._session: Session = db_session

    def query(self, task_id):
        q = self._session.query(*self._orm.query_entity()).filter(MarkTaskTable.id == task_id)
        result = q.one()

        template = TemplateDao(self._session).query(result.id)
        task = self._orm.parse(result, template=template)
        return task

    def list_all(self):
        q = self._session.query(*self._orm.query_entity()).filter(~MarkTaskTable.is_deleted)
        result_list = q.all()

        task_list: List[MarkTask] = []
        for result in result_list:
            template = TemplateDao(self._session).query(result.id)
            task = self._orm.parse(result, template=template)
            task_list.append(task)
        return task_list

    def update(self, task: MarkTask):
        q = self._session.query(*self._orm.query_entity()).filter(MarkTaskTable.id == task.id)
        row = self._orm.serialize(task)
        q.update(row)
        self._session.flush()

    def create(self, new_task: MarkTask):
        TemplateDao(self._session).create(new_task.template)
        row = self._orm.serialize(new_task)
        insert_row = MarkTaskTable(**row)
        self._session.add(insert_row)
        self._session.flush()

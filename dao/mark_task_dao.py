from typing import List

from sqlalchemy.orm import Session

from dao.template_dao import TemplateDao
from domain.mark_task import MarkTask
from table.mark_task_table import MarkTaskTable


class MarkTaskDao:

    _query_entity = [
        MarkTaskTable.id,
        MarkTaskTable.group_id,
        MarkTaskTable.mark_task_result
    ]

    def __init__(self, db_session):
        self._session: Session = db_session

    def query(self, task_id):
        q = self._session.query(*self._query_entity).filter(MarkTaskTable.id == task_id)
        result = q.one()

        template = TemplateDao(self._session).query(result.id)
        task = MarkTask(
            task_id=result.id,
            group_id=result.group_id,
            mark_data=result.mark_task_result,
            template=template
        )
        return task

    def list_all(self):
        q = self._session.query(*self._query_entity).filter(~MarkTaskTable.is_deleted)
        result_list = q.all()

        task_list: List[MarkTask] = []
        for result in result_list:
            template = TemplateDao(self._session).query(result.id)
            task = MarkTask(
                task_id=result.id,
                group_id=result.group_id,
                mark_data=result.mark_task_result,
                template=template
            )
            task_list.append(task)
        return task_list

    def update(self, task: MarkTask):
        q = self._session.query(*self._query_entity).filter(MarkTaskTable.id == task.id)

        row = dict(
            id=task.id,
            group_id=task._group_id,
            mark_task_result=task._mark_data
        )
        q.update(row)
        self._session.flush()

    def create(self, new_task: MarkTask):
        TemplateDao(self._session).create(new_task.template)
        insert_row = MarkTaskTable(
            id=new_task.id,
            group_id=new_task._group_id,
            mark_task_result=new_task._mark_data,
            is_deleted=False
        )
        self._session.add(insert_row)
        self._session.flush()

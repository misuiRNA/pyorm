from typing import List

from config.my_session import session
from dao.template_dao import TemplateDao
from domain.mark_task import MarkTask
from table.mark_task_table import MarkTaskTable


class MarkTaskDao:

    _query_entity = [
        MarkTaskTable.id,
        MarkTaskTable.group_id,
        MarkTaskTable.mark_task_result

    ]

    @classmethod
    def query(cls, task_id):
        q = session.query(*cls._query_entity).filter(MarkTaskTable.id == task_id)
        result = q.one()

        template = TemplateDao.query(result.id)
        task = MarkTask(
            task_id=result.id,
            group_id=result.group_id,
            mark_data=result.mark_task_result,
            template=template
        )
        return task

    @classmethod
    def list_all(cls):
        q = session.query(*cls._query_entity).filter(~MarkTaskTable.is_deleted)
        result_list = q.all()

        task_list: List[MarkTask] = []
        for result in result_list:
            template = TemplateDao.query(result.id)
            task = MarkTask(
                task_id=result.id,
                group_id=result.group_id,
                mark_data=result.mark_task_result,
                template=template
            )
            task_list.append(task)
        return task_list

    @classmethod
    def update(cls, task: MarkTask):
        q = session.query(*cls._query_entity).filter(MarkTaskTable.id == task.id)

        row = dict(
            id=task.id,
            group_id=task._group_id,
            mark_task_result=task._mark_data
        )
        q.update(row)
        session.flush()

    @classmethod
    def create(cls, new_task: MarkTask):
        TemplateDao.create(new_task.template)
        insert_row = MarkTaskTable(
            id=new_task.id,
            group_id=new_task._group_id,
            mark_task_result=new_task._mark_data,
            is_deleted=False
        )
        session.add(insert_row)
        session.flush()

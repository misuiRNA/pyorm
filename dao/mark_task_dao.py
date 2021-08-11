from typing import List

from dao.abstract_dao import AbstractDao
from dao.template_dao import TemplateDao
from domain.mark_task import MarkTask
from sql_executor import SqlExecutor
from table.mark_task_table import MarkTaskTable


class MarkTaskDao(AbstractDao):

    _domain = MarkTask
    _ormapping = {
        "id":       MarkTaskTable.id,
        "group_id": MarkTaskTable.group_id,
    }

    @classmethod
    def get_by_id(cls, task_id):
        executor = SqlExecutor(cls())
        q = executor.query().filter(MarkTaskTable.id == task_id)
        task: MarkTask = executor.one(q)

        tmp = TemplateDao.get_by_id(task.id)
        task.d_i(tmp)
        return task

    @classmethod
    def list(cls):
        executor = SqlExecutor(cls())
        q = executor.query()
        task_list: List[MarkTask] = executor.list_all(q)

        for task in task_list:
            tmp = TemplateDao.get_by_id(task.id)
            task.d_i(tmp)

        return task_list

    @classmethod
    def create(cls, new_task: MarkTask):
        row_list = cls.insert_raws(new_task)
        template_rows = TemplateDao.insert_raws(new_task._template)
        row_list.extend(template_rows)

        executor = SqlExecutor(cls())
        executor.insert(row_list)

    @classmethod
    def insert_raws(cls, task: MarkTask):
        row = SqlExecutor(cls()).row_with_single_table(task)
        return [row]

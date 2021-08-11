from typing import List

from dao.mark_task_dao import MarkTaskDao
from domain.mark_task import MarkTask
from domain.template import Template
from test.title_printer.mark_task_title import MarkTaskTitle
from test.title_printer.printer import print_title
from config.my_session import session


@print_title(MarkTaskTitle)
def do_test():
    task_list: List[MarkTask] = MarkTaskDao.list()
    for task in task_list:
        task.print()

    new_task = _make_task()
    MarkTaskDao.create(new_task)
    session.commit()

    MarkTaskTitle.print_cut_line()

    task_list: List[MarkTask] = MarkTaskDao.list()
    for task in task_list:
        task.print()


def _make_task():
    new_template = Template()
    new_task = MarkTask()
    new_task._template = new_template
    new_task._group_id = 100
    return new_task


if __name__ == "__main__":
    do_test()


from config.my_session import session
from dao.mark_task_dao import MarkTaskDao
from domain.mark_task import MarkTask
from domain.template import Template
from test.title_printer.mark_task_title import MarkTaskTitle
from test.title_printer.printer import print_title, all_diff


@print_title(MarkTaskTitle)
@all_diff(MarkTaskDao)
def do_test():
    new_tmp = Template(tmp_id=0, doctype_id=0, status=0, tmp_data={})
    new_task = MarkTask(task_id=0, group_id=100, mark_data={}, template=new_tmp)

    MarkTaskDao.create(new_task)
    session.commit()


if __name__ == "__main__":
    do_test()


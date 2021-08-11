from config.my_session import session
from dao.template_dao import TemplateDao
from domain.template import Template
from test.title_printer.printer import print_title
from test.title_printer.template_title import TemplateTitle


@print_title(TemplateTitle)
def do_test():
    tmp_id = 239

    tmp: Template = TemplateDao.get_by_id(tmp_id)
    tmp.print()

    _tmp_business(tmp)

    TemplateDao.update(tmp)
    session.commit()

    TemplateTitle.print_cut_line()

    tmp: Template = TemplateDao.get_by_id(tmp_id)
    tmp.print()


def _tmp_business(tmp):
    if not tmp.is_useful():
        tmp.flash({"key_Di": "La La La"})
        tmp.trained()
    else:
        tmp.flash({})
        tmp.trained(0)


if __name__ == "__main__":
    do_test()


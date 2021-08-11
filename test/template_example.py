from config.my_session import session
from dao.template_dao import TemplateDao
from test.title_printer.printer import print_title, one_diff
from test.title_printer.template_title import TemplateTitle


tmp_id = 239


@print_title(TemplateTitle)
@one_diff(TemplateDao, tmp_id)
def do_test():
    tmp = TemplateDao.query(tmp_id)
    if tmp.useful():
        tmp.flash({})
    else:
        tmp.flash({"key_Di": "La La La"})
    TemplateDao.update(tmp)
    session.commit()


if __name__ == "__main__":
    do_test()


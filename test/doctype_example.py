from dao.doctype_dao import DoctypeDao
from test.title_printer.doctype_title import DoctypeTitle
from test.title_printer.printer import print_title


@print_title(DoctypeTitle)
def do_test():
    start, limit_num, search = 0, 10, ""

    count = DoctypeDao.total_count()
    print(f"count = {count}")

    doctype_list = DoctypeDao.list_all(start, limit_num, search)
    for doctype in doctype_list:
        doctype.do_something()


if __name__ == "__main__":
    do_test()

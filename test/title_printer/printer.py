

def print_title(printer):

    def decorator(function):
        def real_func():
            printer.print_head()
            function()
            printer.print_end()
        return real_func

    return decorator


def one_diff(dao, _id):

    def decorator(function):
        def real_func():
            entity = dao.query(_id)
            entity.print()
            print("\n")
            function()
            entity = dao.query(_id)
            entity.print()
        return real_func

    return decorator


def all_diff(dao):

    def print_all():
        entity_list = dao.list_all()
        for entity in entity_list:
            entity.print()

    def decorator(function):
        def real_func():
            print_all()
            print("\n")
            function()
            print_all()
        return real_func

    return decorator

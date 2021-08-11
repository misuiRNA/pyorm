

def print_title(printer):

    def decorator(function):
        def real_func():
            printer.print_head()
            function()
            printer.print_end()
        return real_func

    return decorator

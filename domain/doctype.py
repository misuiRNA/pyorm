class Doctype:

    def __init__(self):
        self._doctype_id = 0
        self._doctype_name = ""
        self._desc = ""
        self._group_count = 0
        self._create_time = None
        self._last_update_time = None

    def do_something(self):
        print("|%-5d" % self._doctype_id, end="")
        print(f"|%-15d" % self._group_count, end="")
        print(f"|%-20s" % self._create_time, end="")
        print(f"|%-20s" % self._last_update_time, end="")
        print(f"|%-15s" % self._desc, end="")
        print(f"|%-15s" % self._doctype_name, end="")
        print("")

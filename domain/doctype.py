class Doctype:

    def __init__(self, doctype_id, doctype_name, desc, group_count, create_time, last_update_time):
        self._doctype_id = doctype_id
        self._doctype_name = doctype_name
        self._desc = desc
        self._group_count = group_count
        self._create_time = create_time
        self._last_update_time = last_update_time

    def do_something(self):
        print("|%-5d" % self._doctype_id, end="")
        print(f"|%-15d" % self._group_count, end="")
        print(f"|%-20s" % self._create_time, end="")
        print(f"|%-20s" % self._last_update_time, end="")
        print(f"|%-15s" % self._desc, end="")
        print(f"|%-15s" % self._doctype_name, end="")
        print("")

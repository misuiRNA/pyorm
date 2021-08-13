class Doctype:

    def __init__(self, id, doctype_id, name, desc, group_count):
        self._doctype_id = doctype_id
        self._doctype_name = name
        self._desc = desc
        self._group_count = group_count

    def do_something(self):
        print("|%-5d" % self._doctype_id, end="")
        print(f"|%-15d" % self._group_count, end="")
        print(f"|%-15s" % self._desc, end="")
        print(f"|%-15s" % self._doctype_name, end="")
        print("")

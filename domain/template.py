class Template:

    def __init__(self):
        self._id = 0
        self._doctype_id = 0
        self._status = -1
        self._tmp_data = {}

    @property
    def id(self):
        return self._id

    def flash(self, json_data):
        self._tmp_data = json_data

    def is_useful(self):
        return self._status > 0

    def trained(self, value=2):
        self._status = value

    def print(self):
        print("|%-6d" % self._id, end="")
        print("|%-11d" % self._doctype_id, end="")
        print("|%-7d" % self._status, end="")
        print(f"|{self._tmp_data}", end="")

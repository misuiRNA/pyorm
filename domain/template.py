class Template:

    def __init__(self, id, doctype_id, status, tmp_data):
        self._id = id
        self._doctype_id = doctype_id
        self._status = status
        self._tmp_data = tmp_data

    @property
    def id(self):
        return self._id

    def flash(self, json_data):
        self._tmp_data = json_data
        if json_data:
            self._status = 2
        else:
            self._status = 0

    def useful(self):
        return self._status > 0

    def print(self):
        print("|%-6d" % self._id, end="")
        print("|%-11d" % self._doctype_id, end="")
        print("|%-7d" % self._status, end="")
        print(f"|{self._tmp_data}", end="")
        print("")

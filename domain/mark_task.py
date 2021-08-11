from domain.template import Template


class MarkTask:

    def __init__(self, task_id, group_id, mark_data, template):
        self._id = task_id
        self._group_id = group_id
        self._mark_data = mark_data
        self._tmp: Template = template

    @property
    def id(self):
        return self._id

    @property
    def template(self):
        return self._tmp

    def re_mark(self, mark_data):
        self._mark_data = mark_data

    def flush_tmp(self):
        self._tmp.flash(self._mark_data)

    def print(self):
        print("|%-6d" % self._id, end="")
        print("|%-9d" % self._group_id, end="")
        print("|%-12d" % self._tmp.id, end="")
        print("")

from domain.template import Template


class MarkTask:

    def __init__(self):
        self._id = 0
        self._group_id = 0
        self._mark_data = {}
        self._template: Template = None

    def d_i(self, template: Template, **kwargs):
        self._template = template

    @property
    def id(self):
        return self._id

    def re_mark(self, mark_data):
        self._mark_data = mark_data

    def flush_tmp(self):
        self._template.flash(self._mark_data)

    def print(self):
        print("|%-6d" % self._id, end="")
        print("|%-9d" % self._group_id, end="")
        print("|%-12d" % self._template.id, end="")
        print("")

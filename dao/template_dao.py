from dao.abstract_dao import AbstractDao
from domain.template import Template
from sql_executor import SqlExecutor
from table.template_table import TemplateTable


class TemplateDao(AbstractDao):

    _domain = Template
    _ormapping = {
        "id":         TemplateTable.id,
        "doctype_id": TemplateTable.doc_type_id,
        "status":     TemplateTable.status,
        "tmp_data":   TemplateTable.config
    }

    @classmethod
    def get_by_id(cls, tmp_id):
        executor = SqlExecutor(cls())
        q = executor.query()\
            .filter(TemplateTable.id == tmp_id)
        template = executor.one(q)
        return template

    @classmethod
    def update(cls, template: Template):
        executor = SqlExecutor(cls())
        executor.update(template)

    @classmethod
    def create(cls, new_tmp: Template):
        raise Exception("can't create Template without MarkTask !")

    @classmethod
    def insert_raws(cls, template: Template):
        row = SqlExecutor(cls()).row_with_single_table(template)
        return [row]


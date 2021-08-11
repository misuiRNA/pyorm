from typing import List

from config.my_session import session
from domain.template import Template
from table.template_table import TemplateTable


class TemplateDao:

    @classmethod
    def query(cls, tmp_id):
        q = session.query(
            TemplateTable.id,
            TemplateTable.doc_type_id,
            TemplateTable.status,
            TemplateTable.config
        ).filter(TemplateTable.id == tmp_id)
        result = q.one()

        template = Template(
            tmp_id=result.id,
            doctype_id=result.doc_type_id,
            status=result.status,
            tmp_data=result.config
        )
        return template

    @classmethod
    def list_all(cls):
        q = session.query(
            TemplateTable.id,
            TemplateTable.doc_type_id,
            TemplateTable.status,
            TemplateTable.config
        )
        result_list = q.all()

        tmp_list: List[Template] = []
        for result in result_list:
            tmp = Template(
                tmp_id=result.id,
                doctype_id=result.doc_type_id,
                status=result.status,
                tmp_data=result.config
            )
            tmp_list.append(tmp)
        return tmp_list

    @classmethod
    def update(cls, template: Template):
        q = session.query(
            TemplateTable.id,
            TemplateTable.doc_type_id,
            TemplateTable.status,
            TemplateTable.config
        ).filter(TemplateTable.id == template.id)

        row = dict(
            id=template.id,
            doc_type_id=template._doctype_id,
            status=template._status,
            config=template._tmp_data
        )
        q.update(row)
        session.flush()

    @classmethod
    def create(cls, new_tmp: Template):
        insert_row = TemplateTable(
            id=new_tmp.id,
            doc_type_id=new_tmp._doctype_id,
            status=new_tmp._status,
            config=new_tmp._tmp_data
        )
        session.add(insert_row)
        session.flush()

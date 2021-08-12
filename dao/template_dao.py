from typing import List

from domain.template import Template
from table.template_table import TemplateTable


class TemplateDao:

    _query_entity = [
        TemplateTable.id,
        TemplateTable.doc_type_id,
        TemplateTable.status,
        TemplateTable.config
    ]

    def __init__(self, db_session):
        self._session = db_session

    def query(self, tmp_id):
        q = self._session.query(*self._query_entity).filter(TemplateTable.id == tmp_id)
        result = q.one()

        template = Template(
            tmp_id=result.id,
            doctype_id=result.doc_type_id,
            status=result.status,
            tmp_data=result.config
        )
        return template

    def list_all(self):
        q = self._session.query(*self._query_entity).filter(~TemplateTable.is_deleted)
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

    def update(self, template: Template):
        q = self._session.query(*self._query_entity).filter(TemplateTable.id == template.id)

        row = dict(
            id=template.id,
            doc_type_id=template._doctype_id,
            status=template._status,
            config=template._tmp_data
        )
        q.update(row)
        self._session.flush()

    def create(self, new_tmp: Template):
        insert_row = TemplateTable(
            id=new_tmp.id,
            doc_type_id=new_tmp._doctype_id,
            status=new_tmp._status,
            config=new_tmp._tmp_data
        )
        self._session.add(insert_row)
        self._session.flush()

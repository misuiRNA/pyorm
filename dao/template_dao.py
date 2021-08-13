from typing import List

from sqlalchemy.orm import Session

from base.ormapper import ORMapper
from domain.template import Template
from table.template_table import TemplateTable


class TemplateDao:
    _mapping = dict(
        id=TemplateTable.id,
        doctype_id=TemplateTable.doc_type_id,
        status=TemplateTable.status,
        tmp_data=TemplateTable.config
    )
    _orm = ORMapper(Template, _mapping)

    def __init__(self, db_session):
        self._session: Session = db_session

    def query(self, tmp_id):
        q = self._session.query(*self._orm.query_entity()).filter(TemplateTable.id == tmp_id)
        result = q.one()

        template = self._orm.parse(result)
        return template

    def list_all(self):
        q = self._session.query(*self._orm.query_entity()).filter(~TemplateTable.is_deleted)
        result_list = q.all()

        tmp_list: List[Template] = []
        for result in result_list:
            tmp = self._orm.parse(result)
            tmp_list.append(tmp)
        return tmp_list

    def update(self, template: Template):
        q = self._session.query(*self._orm.query_entity()).filter(TemplateTable.id == template.id)

        row_dict = self._orm.serialize(template)
        q.update(row_dict)
        self._session.flush()

    def create(self, new_tmp: Template):
        metadata = self._orm.serialize(new_tmp)
        insert_row = TemplateTable(**metadata)
        self._session.add(insert_row)
        self._session.flush()

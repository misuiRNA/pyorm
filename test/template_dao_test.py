from dao.template_dao import TemplateDao
from domain.template import Template
from table.template_table import TemplateTable
from test.AbstractTest import AbstractTest


class TemplateDaoTest(AbstractTest):

    def setUp(self):
        super(TemplateDaoTest, self).setUp()
        
        self.init_data = [
            TemplateTable(is_deleted=False, status=2, doc_type_id=8, config={}),
            TemplateTable(is_deleted=False, status=2, doc_type_id=9, config={"key": 5}),
            TemplateTable(is_deleted=False, status=2, doc_type_id=9, config={"anchor": 666})
        ]
        self._session.add_all(self.init_data)
        self._session.commit()

    def test_query_template_should_success(self):
        query_id = 1
        template = TemplateDao(self._session).query(query_id)
        self.assertEqual(8, template._doctype_id)

    def test_list_template_should_success(self):
        tmp_list = TemplateDao(self._session).list_all()
        self.assertEqual(len(self.init_data), len(tmp_list))

    def test_update_template_should_success(self):
        query_id = 3
        template = TemplateDao(self._session).query(query_id)
        self.assertEqual(2, template._status)

        template.flash({})
        TemplateDao(self._session).update(template)
        self._session.commit()

        template = TemplateDao(self._session).query(query_id)
        self.assertEqual(0, template._status)

    def test_create_template_should_success(self):
        init_len = len(self.init_data)

        tmp_list = TemplateDao(self._session).list_all()
        self.assertEqual(init_len, len(tmp_list))

        new_tmp = Template(tmp_id=-1, doctype_id=15, status=3, tmp_data={"data": "new"})
        TemplateDao(self._session).create(new_tmp)
        self._session.commit()
        init_len = init_len + 1

        tmp_list = TemplateDao(self._session).list_all()
        self.assertEqual(init_len, len(tmp_list))

        template = TemplateDao(self._session).query(tmp_id=-1)
        self.assertEqual(3, template._status)


from dao.template_dao import TemplateDao
from domain.template import Template
from table.template_table import TemplateTable
from test.abstract_test import AbstractTest


class TemplateDaoTest(AbstractTest):

    def setUp(self):
        super(TemplateDaoTest, self).setUp()
        self._dao = TemplateDao(self._session)

        self.mock_data = [
            TemplateTable(is_deleted=False, status=2, doc_type_id=8, config={}),
            TemplateTable(is_deleted=False, status=2, doc_type_id=9, config={"key": 5}),
            TemplateTable(is_deleted=False, status=2, doc_type_id=9, config={"anchor": 666})
        ]
        self._session.add_all(self.mock_data)
        self._session.commit()

    def test_query_template_should_success(self):
        query_id = 1
        template = self._dao.query(query_id)
        self.assertEqual(8, template._doctype_id)

    def test_list_template_should_success(self):
        tmp_list = self._dao.list_all()
        self.assertEqual(len(self.mock_data), len(tmp_list))

    def test_update_template_should_success(self):
        query_id = 3
        template = self._dao.query(query_id)
        self.assertEqual(2, template._status)

        template.flash({})
        self._dao.update(template)
        self._session.commit()

        template = self._dao.query(query_id)
        self.assertEqual(0, template._status)

    def test_create_template_should_success(self):
        expected_len = len(self.mock_data)

        tmp_list = self._dao.list_all()
        self.assertEqual(expected_len, len(tmp_list))

        new_tmp = Template(tmp_id=20, doctype_id=15, status=3, tmp_data={"data": "new"})
        self._dao.create(new_tmp)
        self._session.commit()
        expected_len = expected_len + 1

        tmp_list = self._dao.list_all()
        self.assertEqual(expected_len, len(tmp_list))

        template = self._dao.query(tmp_id=20)
        self.assertEqual(3, template._status)


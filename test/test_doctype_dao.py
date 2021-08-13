from dao.doctype_dao import DoctypeDao
from table.doctype_table import DocTypeTable
from table.mark_task_group_table import MarkTaskGroupTable
from test.abstract_test import AbstractTest


class DoctypeDaoTest(AbstractTest):

    def setUp(self):
        super(DoctypeDaoTest, self).setUp()
        self._dao = DoctypeDao(self._session)

        self.mock_data = [
            DocTypeTable(id=1, is_deleted=False, name="doc_1", desc="Diu Diu Diu"),
            MarkTaskGroupTable(is_deleted=False, name="group_11", doc_type_id=1),
            MarkTaskGroupTable(is_deleted=False, name="group_12", doc_type_id=1),
            MarkTaskGroupTable(is_deleted=False, name="group_13", doc_type_id=1),

            DocTypeTable(id=2, is_deleted=False, name="doc_2", desc="Diu Diu Diu"),
            MarkTaskGroupTable(is_deleted=False, name="group_21", doc_type_id=2),
            MarkTaskGroupTable(is_deleted=False, name="group_22", doc_type_id=2),

            DocTypeTable(id=3, is_deleted=False, name="doc_3", desc="Diu Diu Diu"),
            MarkTaskGroupTable(is_deleted=False, name="group_31", doc_type_id=3),
            MarkTaskGroupTable(is_deleted=False, name="group_32", doc_type_id=3),
            MarkTaskGroupTable(is_deleted=False, name="group_33", doc_type_id=3),
            MarkTaskGroupTable(is_deleted=False, name="group_34", doc_type_id=3),
            MarkTaskGroupTable(is_deleted=False, name="group_35", doc_type_id=3),
            MarkTaskGroupTable(is_deleted=False, name="group_36", doc_type_id=3),
        ]
        self._session.add_all(self.mock_data)
        self._session.commit()

    def test_list_doctype_should_success(self):
        doctype_list = self._dao.list_all(0, 10, "")
        self.assertEqual(3, len(doctype_list))

    def test_count_doctype_should_success(self):
        count = self._dao.total_count()
        self.assertEqual(3, count)



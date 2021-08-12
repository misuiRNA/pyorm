from dao.mark_task_dao import MarkTaskDao
from domain.mark_task import MarkTask
from domain.template import Template
from table.mark_task_table import MarkTaskTable
from table.template_table import TemplateTable
from test.AbstractTest import AbstractTest


class MarkTaskDaoTest(AbstractTest):

    def setUp(self):
        super(MarkTaskDaoTest, self).setUp()

        self.init_data = [
            MarkTaskTable(is_deleted=False, group_id=1, mark_task_result={}),
            TemplateTable(is_deleted=False, status=2, doc_type_id=8, config={}),

            MarkTaskTable(is_deleted=False, group_id=1, mark_task_result={"data": "Di Di Di"}),
            TemplateTable(is_deleted=False, status=2, doc_type_id=8, config={}),

            MarkTaskTable(is_deleted=False, group_id=1, mark_task_result={"data": "La La La"}),
            TemplateTable(is_deleted=False, status=2, doc_type_id=8, config={}),
        ]
        self._session.add_all(self.init_data)
        self._session.commit()

    def test_query_task_should_success(self):
        query_id = 1
        task = MarkTaskDao(self._session).query(query_id)
        self.assertEqual(1, task._group_id)

    def test_list_task_should_success(self):
        task_list = MarkTaskDao(self._session).list_all()
        self.assertEqual(3, len(task_list))

    def test_update_task_should_success(self):
        query_id = 3
        task = MarkTaskDao(self._session).query(query_id)
        self.assertEqual(1, task._group_id)

        task._group_id = 2
        MarkTaskDao(self._session).update(task)
        self._session.commit()

        task = MarkTaskDao(self._session).query(query_id)
        self.assertEqual(2, task._group_id)

    def test_create_template_should_success(self):
        init_len = 3

        task_list = MarkTaskDao(self._session).list_all()
        self.assertEqual(init_len, len(task_list))

        new_tmp = Template(tmp_id=-1, doctype_id=15, status=3, tmp_data={"data": "new"})
        new_task = MarkTask(task_id=-1, group_id=5, mark_data={}, template=new_tmp)
        MarkTaskDao(self._session).create(new_task)
        self._session.commit()
        init_len = init_len + 1

        tmp_list = MarkTaskDao(self._session).list_all()
        self.assertEqual(init_len, len(tmp_list))

        task = MarkTaskDao(self._session).query(task_id=-1)
        self.assertEqual(5, task._group_id)


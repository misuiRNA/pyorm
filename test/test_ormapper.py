import unittest

from base.ormapper import ORMapper
from table.template_table import TemplateTable


class ORMapperTest(unittest.TestCase):

    _mapping = {
        "doctype_id": TemplateTable.id,
        "state": TemplateTable.status
    }

    class TestType:

        def __init__(self, doctype_id, state):
            self._doctype_id = doctype_id
            self._state = state

    def test_construct_should_success(self):
        orm = ORMapper(self.TestType, self._mapping)
        self.assertTrue(isinstance(orm, ORMapper))

    def test_construct_with_non_type_should_error(self):
        self.assertRaises(
            AssertionError,
            ORMapper,

            self.TestType(1, "test"),
            self._mapping
        )

    def test_construct_with_unmatched_mapping_should_error(self):

        _mapping = {
            "id": TemplateTable.id,
            "value": TemplateTable.status
        }

        self.assertRaises(
            TypeError,
            ORMapper,

            self.TestType,
            _mapping
        )

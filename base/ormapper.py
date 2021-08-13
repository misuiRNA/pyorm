

class ORMapper:

    def __init__(self, domain_class, mapping):
        self._class: type = domain_class
        self._mapping: dict = mapping
        self._assert_conf()

    def query_entity(self):
        pattern = []
        for attr, table_column in self._mapping.items():
            pattern.append(table_column.label(attr))
        return pattern

    def parse(self, result, **kwargs):
        if not result:
            return None

        param_list = {}
        for attr, value in self._mapping.items():
            if not hasattr(result, attr):
                raise Exception(f"can't find attr '{attr}' in sql query result !")
            param_list.update({
                attr: getattr(result, attr)
            })
        param_list.update(kwargs)
        domain = self._class(**param_list)
        return domain

    def serialize(self, domain):
        assert domain, "'domain' is empty !"

        metadata = {}
        for attr in self._mapping:
            value = getattr(domain, f"_{attr}")
            column_name = self._mapping[attr].key
            metadata.update({
                column_name: value
            })
        return metadata

    def _assert_conf(self):
        assert isinstance(self._class, type), f"'{self._class}' is not a class !"
        assert self._class(**self._mapping)

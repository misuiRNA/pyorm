

class AbstractDao:

    _domain = None
    _ormapping = None
    _union_table = None

    def domain(self):
        if self._domain is None:
            raise Exception("has not init attribute '_domain'")
        return self._domain

    def ormapping(self):
        if self._ormapping is None:
            raise Exception("has not init attribute '_ormapping'")
        return self._ormapping

    def union_table(self):
        return self._union_table




# -*- coding: utf-8 -*-


from modules.shared.domain.bus.query import Query


class StoreFinderQuery(Query):
    """
    Store finder query
    """

    def __init__(self,
                 id: str):
        self.__id = id

    @property
    def id(self):
        return self.__id
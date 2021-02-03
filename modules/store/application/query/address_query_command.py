
# -*- coding: utf-8 -*-


from modules.shared.domain.bus.query import Query


class AddressFinderQuery(Query):
    """
    Address finder query
    """

    def __init__(self,
                 id: str = None):
        self.__id = id

    @property
    def id(self):
        """
        Id property
        """
        return self.__id

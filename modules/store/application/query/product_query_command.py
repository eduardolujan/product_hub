
# -*- coding: utf-8 -*-

from modules.shared.domain.bus.query import Query


class ProductFinderQuery(Query):
    """
    Product finder query
    """

    def __init__(self, id: str):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def sku(self):
        return self.__sku

    @property
    def store_id(self):
        return self.__store_id


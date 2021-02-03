
# -*- coding: utf-8 -*-


from modules.shared.domain.bus.command import Command


class ProductCreateCommand(Command):
    """
    Product Create Command
    """

    def __init__(self,
                 id: str,
                 name: str,
                 price: float,
                 sku: str,
                 store_id: str):

        self.__id = id
        self.__name = name
        self.__price = price
        self.__sku = sku
        self.__store_id = store_id

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
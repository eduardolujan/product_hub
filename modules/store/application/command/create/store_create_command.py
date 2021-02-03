
# -*- coding: utf-8 -*-


from modules.shared.domain.bus.command import Command


class StoreCreateCommand(Command):
    """
    Store Create Command
    """

    def __init__(self,
                 id: str,
                 name: str):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
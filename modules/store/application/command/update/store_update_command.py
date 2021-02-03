
# -*- coding: utf-8 -*-


from modules.shared.domain.bus.command import Command


class StoreUpdateCommand(Command):
    """
    Store Create Command
    """

    def __init__(self,
                 name: str):
        self.__name = name

    @property
    def name(self):
        """
        Name property
        @return: name
        @rtype: str
        """
        return self.__name
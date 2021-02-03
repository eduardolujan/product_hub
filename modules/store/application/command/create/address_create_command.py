
# -*- coding: utf-8 -*-


from modules.shared.domain.bus.command import Command


class AddressCreateCommand(Command):
    """
    Store Create Command
    """

    def __init__(self,
                 id: str = None,
                 street: str = None,
                 external_number: str = None,
                 internal_number: str = None,
                 city: str = None,
                 state: str = None,
                 country: str = None,
                 zipcode: str = None,
                 store_id: str = None):

        self.__id = id
        self.__street = street
        self.__external_number = external_number
        self.__internal_number = internal_number
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode
        self.__store_id = store_id

    @property
    def id(self):
        """
        Id property
        """
        return self.__id

    @property
    def street(self):
        """
        Street property
        """
        return self.__street

    @property
    def external_number(self):
        """
        External number property
        """
        return self.__external_number

    @property
    def internal_number(self):
        """
        Internal number property
        """
        return self.__internal_number

    @property
    def city(self):
        """
        External number property
        """
        return self.__city

    @property
    def state(self):
        """
        State property
        """
        return self.__state

    @property
    def country(self):
        """
        Internal number property
        """
        return self.__country

    @property
    def zipcode(self):
        """
        Zipcode property
        """
        return self.__zipcode

    @property
    def store_id(self):
        """
        Store id property
        """
        return self.__store_id






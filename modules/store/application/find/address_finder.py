
# -*- coding: utf-8 -*-


from typing import NoReturn

from modules.store.domain.repository import AddressRepository
from modules.store.domain.exceptions import AddressNotExist
from modules.shared.domain.bus.query import Query


class AddressFinder:
    """
    Address finder
    """

    def __init__(self, address_repository: AddressRepository):
        """
        Constructor
        @param address_repository:
        @type address_repository:
        """
        self.__address_repository = address_repository

    def __call__(self, address_finder_query: Query) -> NoReturn:
        address = self.__address_repository.get(address_finder_query.id)

        if not address:
            raise AddressNotExist(f"Address not exist {address_finder_query.id}")

        return address

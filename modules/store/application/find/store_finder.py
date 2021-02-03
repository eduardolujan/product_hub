
# -*- coding: utf-8 -*-


from typing import NoReturn

from modules.store.domain.repository import StoreRepository
from modules.store.domain.exceptions import StoreNotExist
from modules.shared.domain.bus.query import Query


class StoreFinder:
    """
    Store Finder
    """

    def __init__(self, store_respository: StoreRepository) -> NoReturn:
        if not isinstance(store_respository, StoreRepository):
            raise Exception(f"Error {store_respository} is no instance of StoreRepository")

        self.__store_respository = store_respository

    def __call__(self, store_finder_query: Query) -> NoReturn:
        """
        Caller store finder
        @param store_finder_query: Store finder command
        @type store_finder_query: StoreFinderCommand
        @return: No return
        @rtype: NoReturn
        """
        store = self.__store_respository.get(store_finder_query.id)
        if not store:
            raise StoreNotExist(f"Store doesn't exists {store_finder_query.id}")

        return store


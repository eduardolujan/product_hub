
# -*- coding: utf-8 -*-


from typing import NoReturn

from modules.store.domain.repository import StoreRepository


class StoreSearcher:
    """
    Store Finder
    """

    def __init__(self, store_respository: StoreRepository) -> NoReturn:
        if not isinstance(store_respository, StoreRepository):
            raise Exception(f"Error {store_respository} is not instance of StoreRepository")

        self.__store_respository = store_respository

    def __call__(self) -> NoReturn:
        """
        Caller store searcher
        @return: No return
        @rtype: NoReturn
        """
        return self.__store_respository.searcher()



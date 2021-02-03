
# -*- coding: utf-8 -*-+


from typing import NoReturn

from modules.store.domain.repository import StoreRepository
from modules.store.domain.services.update import StoreUpdater as StoreUpdaterService
from modules.store.domain.exceptions import StoreNotExist
from modules.shared.domain.bus.command import Command


class StoreDeleter:
    """
    Store Updater
    """

    def __init__(self, store_repository: StoreRepository) -> NoReturn:
        """
        Constructor
        @param store_repository: Store repository
        @type store_repository: StoreRepository
        """
        self.__store_repository = store_repository

    def __call__(self, store_id: str) -> NoReturn:
        """
        Caller delete store
        @return: No return
        @rtype: NoReturn
        """
        if not self.__store_repository.get(store_id):
            raise StoreNotExist(f"Store doesn't exists {store_id}")

        self.__store_repository.delete(store_id)


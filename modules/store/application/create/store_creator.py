
# -*- coding: utf-8 -*-+

from typing import NoReturn

from modules.store.domain.repository import StoreRepository
from modules.store.domain.services.create import StoreCreator as StoreCreatorService
from modules.store.domain.exceptions import StoreAlreadyExists
from modules.shared.domain.bus.command import Command


class StoreCreator:
    """
    Store Creator
    """

    def __init__(self, store_repository: StoreRepository) -> NoReturn:
        """
        Constructor
        @param store_repository: Store repository
        @type store_repository: StoreRepository
        """
        self.__store_repository = store_repository

    def __call__(self, create_store_command: Command) -> NoReturn:
        """
        Caller
        @param create_store_command: Create store command
        @type create_store_command: CreateStoreCommand
        @return: No return
        @rtype: NoReturn
        """

        if self.__store_repository.get(create_store_command.id):
            raise StoreAlreadyExists(f"Store already exists {create_store_command.id}")

        store = StoreCreatorService.create_store(
            id=create_store_command.id,
            name=create_store_command.name
        )
        self.__store_repository.create(store)


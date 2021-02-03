
# -*- coding: utf-8 -*-


from typing import NoReturn

from modules.store.domain.repository import AddressRepository, StoreRepository
from modules.store.domain.services.create import AddressCreator as AddressCreatorService
from modules.store.domain.exceptions import StoreNotExist, AddressAlreadyExists
from modules.shared.domain.bus.command import Command


class AddressUpdater:
    """
    Address Creator
    """

    def __init__(self,
                 address_repository: AddressRepository,
                 store_repository: StoreRepository):
        """
        Constructor
        @param address_repository: Address repository
        @type address_repository: AddressRepository
        @param store_repository: Store repository
        @type store_repository: AddressRepository
        """
        if not isinstance(address_repository, AddressRepository):
            raise Exception(f"Error address_repository: {address_repository} is not instance of AddressRepository")

        if not isinstance(store_repository, StoreRepository):
            raise Exception(f"Error address_repository: {store_repository} is not instance of StoreRepository")

        self.__store_repository = store_repository
        self.__address_repository = address_repository

    def __call__(self, create_store_command: Command) -> NoReturn:
        """
        Caller create store
        @param create_store_command: Create store command
        @type create_store_command: CreateStoreCommand
        @return: No return
        @rtype: NoReturn
        """
        if not self.__store_repository.get(create_store_command.store_id):
            raise StoreNotExist(f"Store id not exists {create_store_command.store_id}")

        if self.__address_repository.get(create_store_command.id):
            raise AddressAlreadyExists(f"Address registry already exists {create_store_command.id}")

        address_entity = AddressCreatorService.create(
            id=create_store_command.id,
            street=create_store_command.street,
            external_number=create_store_command.external_number,
            internal_number=create_store_command.internal_number,
            city=create_store_command.city,
            state=create_store_command.state,
            country=create_store_command.country,
            zipcode=create_store_command.zipcode,
            store_id=create_store_command.store_id
        )
        self.__address_repository.create(address_entity)


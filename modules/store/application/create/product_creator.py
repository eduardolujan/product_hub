
# -*- coding: utf-8 -*-


from typing import NoReturn

from modules.store.domain.repository import ProductRepository, StoreRepository
from modules.store.domain.services.create import ProductCreator as ProductCreatorService
from modules.store.domain.exceptions import ProductAlreadyExists, StoreNotExist
from modules.shared.domain.bus.command import Command


class ProductCreator:
    """
    Product Creator
    """

    def __init__(self,
                 product_repository: ProductRepository,
                 store_repository: StoreRepository):
        """
        Constructor Product creator
        @param product_repository: Product repository
        @type product_repository: ProductRepository
        @param store_repository: Store repository
        @type store_repository: StoreRepository
        """
        if not isinstance(product_repository, ProductRepository):
            raise Exception(f"Error product_repository: {product_repository} is not instance ProductRepository")

        if not isinstance(store_repository, StoreRepository):
            raise Exception(f"Error store_repository: {store_repository} is not instance StoreRepository")

        self.__product_repository = product_repository
        self.__store_repository = store_repository

    def __call__(self, create_product_command: Command) -> NoReturn:
        """
        Caller create product
        @param create_product_command: Create product command
        @type create_product_command: CreateProductCommand
        @return: No return
        @rtype: NoReturn
        """

        if self.__product_repository.get(create_product_command.id):
            raise ProductAlreadyExists(f"Product already exists {create_product_command.id}")

        if not self.__store_repository.get(create_product_command.store_id):
            raise StoreNotExist(f"Store doesn't exists {create_product_command.store_id}")

        create_product_entity = ProductCreatorService.create(
            id=create_product_command.id,
            name=create_product_command.name,
            price=create_product_command.price,
            sku=create_product_command.sku,
            store_id=create_product_command.store_id
        )
        self.__product_repository.create(create_product_entity)


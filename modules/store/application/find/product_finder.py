
# -*- coding: utf-8 -*-


from modules.store.domain.repository import ProductRepository
from modules.store.domain.exceptions import ProductNotExist
from modules.shared.domain.bus.query import Query


class ProductFinder:
    """
    Product finder
    """

    def __init__(self, product_repository: ProductRepository):
        if not isinstance(product_repository, ProductRepository):
            raise Exception(f"Error {product_repository} is no instance of ProductRepository")

        self.__product_repository = product_repository

    def __call__(self, product_finder_query: Query):
        product = self.__product_repository.get(product_finder_query.id)

        if not product:
            raise ProductNotExist(f"Product not exists {product_finder_query.id}")
        return product


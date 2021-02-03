
# -*- coding: utf-8 -*-


from modules.shared.infrastructure.persistence.sqlalchemy import SessionManager
from modules.store.domain.entity import Product as ProductEntity
from modules.store.domain.repository import ProductRepository as AbstractProductRepository
from modules.shared.domain.aggregate import AggregateRoot


class ProductRepository(AbstractProductRepository):
    """
    Product Repository
    """

    def __init__(self, session_manager=None):
        self.__session_manager = session_manager or SessionManager()
        self.__session = self.__session_manager.get_session()

    def get(self, id: str):
        """
        Get product by id
        """
        address = self.__session.query(ProductEntity).get(id)
        return address

    def create(self, create_entity: AggregateRoot):
        """
        Create product by create_entity
        """
        self.__session.add(create_entity)
        try:
            self.__session.commit()
        except Exception as err:
            print(f"Error in {__name__}, err:{err}")


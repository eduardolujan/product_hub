
# -*- coding: utf-8 -*-


from modules.shared.infrastructure.persistence.sqlalchemy import SessionManager
from modules.store.domain.entity import Address as AddressEntity
from modules.store.domain.repository import AddressRepository as AbstractAddressRepository
from modules.shared.domain.aggregate import AggregateRoot


class AddressRepository(AbstractAddressRepository):
    """
    Store Repository
    """

    def __init__(self, session_manager=None):
        self.__session_manager = session_manager or SessionManager()
        self.__session = self.__session_manager.get_session()

    def get(self, id: str):
        """
        Get address by id
        """
        address = self.__session.query(AddressEntity).get(id)
        return address

    def create(self, create_entity: AggregateRoot):
        """
        Create address by create_entity
        """
        self.__session.add(create_entity)
        self.__session.commit()


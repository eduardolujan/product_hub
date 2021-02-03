
# -*- coding: utf-8 -*-

from typing import NoReturn, List

from modules.shared.infrastructure.persistence.sqlalchemy import SessionManager
from modules.store.domain.repository import StoreRepository as AbstractStoreRepository
from modules.store.domain.entity import Store as StoreEntity
from modules.shared.domain.aggregate import AggregateRoot


class StoreRepository(AbstractStoreRepository):
    """
    Store Repository
    """
    def __init__(self, session_manager=None):
        self.__session_manager = session_manager or SessionManager()
        self.__session = self.__session_manager.get_session()

    def get(self, id: str):
        """
        Get store by id
        """
        store = self.__session.query(StoreEntity).get(id)
        return store

    def create(self, create_entity: AggregateRoot) -> NoReturn:
        """
        Create store
        @param create_entity: Store create entity
        @type create_entity: create_entity
        @return: No
        @rtype:
        """
        self.__session.add(create_entity)
        self.__session.commit()

    def update(self, entity_id: str, update_entity: AggregateRoot) -> NoReturn:
        """
        Update store
        @param entity_id: entity id
        @type entity_id: str
        @param update_entity:
        @type update_entity:
        @return:
        @rtype:
        """
        update_data = update_entity.as_dict()
        self.__session.query(StoreEntity).filter(
            StoreEntity.id == entity_id
        ).update(update_data, synchronize_session=False)
        self.__session.commit()

    def delete(self, entity_id: str) -> NoReturn:
        """
        Delete store
        @param entity_id: store_id
        @type entity_id: str
        @return: No return
        @rtype: NoReturn
        """
        self.__session.query(StoreEntity).filter(
            StoreEntity.id == entity_id
        ).delete()
        self.__session.commit()

    def searcher(self) -> List[StoreEntity]:
        """
        Searcher store
        @return: Entity list
        @rtype: list
        """
        return self.__session.query(StoreEntity).all()


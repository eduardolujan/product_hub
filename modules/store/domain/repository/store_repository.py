
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from typing import Optional, List

from modules.store.domain.entity import Store as StoreEntity
from modules.shared.domain.aggregate import AggregateRoot


class StoreRepository(ABC):
    """
    Store Repository
    """

    @abstractmethod
    def get(self, id: str) -> Optional[StoreEntity]:
        """
        Get store
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def create(self, create_entity: AggregateRoot):
        """
        Create store
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def update(self, entity_id: str, update_entity: AggregateRoot):
        """
        Update store
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def delete(self, entity_id: str):
        """
        Delete store
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def searcher(self) -> List[StoreEntity]:
        """
        Searcher
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented yet")



# -*- coding: utf-8 -*-

from typing import Optional, List, NoReturn

from modules.store.domain.entity import Store as StoreEntity
from modules.store.domain.repository import StoreRepository
from modules.shared.domain.aggregate import AggregateRoot


class FakeStoreRepository(StoreRepository):
    """
    Fake store repository
    """

    def __init__(self, items=[]):
        self.__items = items

    def get(self, id: str):
        filtered = filter(lambda store: store.id == id, self.__items)
        items = list(filtered)
        if not items:
            return None
        return items[0]

    def create(self, create_entity: AggregateRoot):
        self.__items.append(create_entity)

    def update(self, entity_id: str, update_entity: AggregateRoot):
        def update_item(item, data):
            item_data = item.as_dict()
            item_data.update(**data)
            return StoreEntity(**item_data)
        self.__items = [
            update_item(item, update_entity.as_dict()) if item else item for item in self.__items
        ]

    def delete(self, entity_id: str):
        self.__items = [
            item for item in self.__items if item.id != entity_id
        ]

    def searcher(self) -> List[StoreEntity]:
        return self.__items

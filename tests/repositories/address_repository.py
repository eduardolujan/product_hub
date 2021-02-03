

from modules.store.domain.repository import AddressRepository
from modules.shared.domain.aggregate import AggregateRoot


class FakeAddressRepository(AddressRepository):
    """
    Fake product repository
    """

    def __init__(self, items=[]):
        self.__items = items

    def get(self, id: str):
        filtered = filter(lambda item: item.id == id, self.__items)
        items = list(filtered)
        if not items:
            return None
        return items[0]

    def create(self, create_entity: AggregateRoot):
        self.__items.append(create_entity)


__all__ = ['FakeAddressRepository']

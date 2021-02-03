
from abc import ABC, abstractmethod

from modules.shared.domain.aggregate import AggregateRoot


class AddressRepository(ABC):
    """
    Store Repository
    """

    @abstractmethod
    def get(self, id: str):
        """
        Get address
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def create(self, create_entity: AggregateRoot):
        """
        Create address
        """
        raise NotImplementedError("Not implemented yet")


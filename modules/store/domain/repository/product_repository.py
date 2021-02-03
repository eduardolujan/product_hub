
from abc import ABC, abstractmethod

from modules.shared.domain.aggregate import AggregateRoot


class ProductRepository(ABC):
    """
    Store Product
    """

    @abstractmethod
    def get(self, id: str):
        """
        Get product
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def create(self, create_entity: AggregateRoot):
        """
        Create product
        """
        raise NotImplementedError("Not implemented yet")


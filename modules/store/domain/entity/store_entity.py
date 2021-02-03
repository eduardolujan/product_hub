

from dataclasses import dataclass

from modules.shared.domain.aggregate import AggregateRoot


@dataclass
class GetStore(AggregateRoot):
    """
    Get Store Entity
    """
    id: str


@dataclass
class Store(AggregateRoot):
    """
    Store Entity
    """
    id: str
    name: str


@dataclass
class UpdateStore(AggregateRoot):
    """
    Update Store Entity
    """
    name: str




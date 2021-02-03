

from dataclasses import dataclass

from modules.shared.domain.aggregate import AggregateRoot


@dataclass
class GetProduct(AggregateRoot):
    """
    Get Product Entity
    """
    id: str


@dataclass
class Product(AggregateRoot):
    """
    Product Entity
    """
    id: str
    name: str
    price: float
    sku: str
    store_id: str



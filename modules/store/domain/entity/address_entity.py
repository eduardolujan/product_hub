
from dataclasses import dataclass

from modules.shared.domain.aggregate import AggregateRoot


@dataclass
class GetAddress(AggregateRoot):
    """
    Get Address Entity
    """
    id: str


@dataclass
class Address(AggregateRoot):
    """
    Address Entity
    """
    id: str
    street: str
    external_number: str
    internal_number: str
    city: str
    state: str
    country: str
    zipcode: str
    store_id: str


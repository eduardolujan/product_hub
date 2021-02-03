

import pytest

from tests.repositories import FakeStoreRepository, FakeAddressRepository
from modules.store.application.find import AddressFinder
from modules.store.application.query import AddressFinderQuery
from modules.store.domain.exceptions import AddressNotExist


def test_address_get_success(address_id, address_entity):
    items = [address_entity]
    address_query_query = AddressFinderQuery(id=address_id)
    fake_store_repository = FakeStoreRepository(items)
    address_finder = AddressFinder(fake_store_repository)
    address = address_finder(address_query_query)
    assert address.id == address_entity.id


def test_address_get_unsuccess(address_id, ):
    items = []
    address_finder_query = AddressFinderQuery(id=address_id)
    fake_address_repository = FakeAddressRepository(items)
    address_finder = AddressFinder(fake_address_repository)
    with pytest.raises(AddressNotExist):
        address_finder(address_finder_query)

import pytest

from tests.repositories import FakeStoreRepository, FakeAddressRepository
from modules.store.application.create import AddressCreator
from modules.store.application.command.create import AddressCreateCommand
from modules.store.domain.exceptions import StoreNotExist


def test_create_address_store_not_exist_fail(address_id, address_data, store_id):
    address_items, store_items = [], []
    fake_address_repository = FakeAddressRepository(address_items)
    fake_store_repository = FakeStoreRepository(store_items)
    address_create_command = AddressCreateCommand(**address_data)
    address_creator = AddressCreator(fake_address_repository, fake_store_repository)

    with pytest.raises(StoreNotExist):
        address_creator(address_create_command)


def test_create_address_success(address_id, address_data, store_id, store_entity):
    address_items, store_items = [], [store_entity]
    fake_address_repository = FakeAddressRepository(address_items)
    fake_store_repository = FakeStoreRepository(store_items)
    address_create_command = AddressCreateCommand(**address_data)
    address_creator = AddressCreator(fake_address_repository, fake_store_repository)
    address_creator(address_create_command)
    address_entity_created = fake_address_repository.get(address_id)

    assert address_entity_created.id == address_id




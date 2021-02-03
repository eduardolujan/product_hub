

import pytest

from tests.repositories.store_repository import FakeStoreRepository

from modules.store.application.update import StoreUpdater
from modules.store.application.command.update import StoreUpdateCommand
from modules.store.domain.exceptions import StoreNotExist


def test_store_update_success_store_exists(store_id, store_entity, store_data):
    stores = [store_entity]
    new_store_name = "Store updated"
    update_store_data = dict(
        name=new_store_name
    )
    store_create_command = StoreUpdateCommand(**update_store_data)
    fake_store_repository = FakeStoreRepository(stores)
    store_updater = StoreUpdater(fake_store_repository)
    store_updater(store_id, store_create_command)
    store_entity = fake_store_repository.get(store_id)
    update_store_data.update(id=store_id)
    assert store_entity.as_dict() == update_store_data


def test_store_update_success_store_not_exists(store_id, store_entity, store_data):
    stores = []
    new_store_name = "Store updated"
    update_store_data = dict(
        name=new_store_name
    )
    store_create_command = StoreUpdateCommand(**update_store_data)
    fake_store_repository = FakeStoreRepository(stores)
    store_updater = StoreUpdater(fake_store_repository)
    with pytest.raises(StoreNotExist):
        store_updater(store_id, store_create_command)


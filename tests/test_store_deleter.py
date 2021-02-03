

import pytest

from tests.repositories.store_repository import FakeStoreRepository
from modules.store.application.delete import StoreDeleter
from modules.store.domain.exceptions import StoreNotExist


def test_store_delete_success_store_exists(store_id, store_entity, store_data):
    stores = [store_entity]
    fake_store_repository = FakeStoreRepository(stores)
    store_updater = StoreDeleter(fake_store_repository)
    store_updater(store_id)
    store_entity = fake_store_repository.get(store_id)
    assert store_entity is None


def test_store_delete_success_store_not_exists(store_id, store_entity, store_data):
    stores = []
    fake_store_repository = FakeStoreRepository(stores)
    store_updater = StoreDeleter(fake_store_repository)
    with pytest.raises(StoreNotExist):
        store_updater(store_id)


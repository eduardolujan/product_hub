

import pytest

from tests.repositories.store_repository import FakeStoreRepository
from modules.store.application.find import StoreFinder
from modules.store.application.query import StoreFinderQuery
from modules.store.domain.exceptions import StoreNotExist


def test_store_get_success_store_id_exists(store_id, store_data, store_entity):
    items = [store_entity]
    fake_store_repository = FakeStoreRepository(items)
    store_finder_query = StoreFinderQuery(id=store_id)
    store_finder = StoreFinder(fake_store_repository)
    store = store_finder(store_finder_query)
    assert store.id == store_id


def test_store_get_unsuccess_not_exist_store_id(store_id, store_data, store_entity):
    items = []
    fake_store_repository = FakeStoreRepository(items)
    store_finder_query = StoreFinderQuery(id=store_id)
    store_finder = StoreFinder(fake_store_repository)
    with pytest.raises(StoreNotExist):
        store_finder(store_finder_query)


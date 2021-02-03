

from tests.repositories.store_repository import FakeStoreRepository

from modules.store.application.create import StoreCreator
from modules.store.application.command.create import StoreCreateCommand


def test_store_create(store_id, store_data):
    items = []
    store_create_command = StoreCreateCommand(**store_data)
    fake_store_repository = FakeStoreRepository(items)
    store_creator = StoreCreator(fake_store_repository)
    store_creator(store_create_command)
    store_entity = fake_store_repository.get(store_id)
    assert type(store_entity) is not None
    assert store_entity.id == store_id

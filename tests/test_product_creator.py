
import pytest

from tests.repositories import FakeStoreRepository, FakeProductRepository
from modules.store.application.create import ProductCreator
from modules.store.application.command.create import ProductCreateCommand
from modules.store.domain.exceptions import StoreNotExist, ProductAlreadyExists


def test_product_get(product_id, product_entity):
    items = [product_entity]
    fake_product_repository = FakeProductRepository(items)
    product_entity_gotten = fake_product_repository.get(product_id)
    assert product_entity.id == product_entity_gotten.id


def test_create_product_store_not_exist_fail(product_data):
    address_items, store_items = [], []

    fake_product_repository = FakeProductRepository(store_items)
    fake_store_repository = FakeStoreRepository(store_items)

    address_create_command = ProductCreateCommand(**product_data)
    with pytest.raises(StoreNotExist) as context:
        address_creator = ProductCreator(fake_product_repository, fake_store_repository)
        address_creator(address_create_command)


def test_create_product_already_exists(product_data, product_entity, store_entity):
    product_items, store_items = [product_entity], [store_entity]

    fake_product_repository = FakeProductRepository(product_items)
    fake_store_repository = FakeStoreRepository(store_items)

    address_create_command = ProductCreateCommand(**product_data)
    with pytest.raises(ProductAlreadyExists):
        address_creator = ProductCreator(fake_product_repository, fake_store_repository)
        address_creator(address_create_command)


def test_create_product_success(product_id, product_data, store_entity):
    product_items, store_items = [], [store_entity]
    fake_product_repository = FakeProductRepository(store_items)
    fake_store_repository = FakeStoreRepository(store_items)
    product_create_command = ProductCreateCommand(**product_data)
    product_creator = ProductCreator(fake_product_repository, fake_store_repository)
    product_creator(product_create_command)
    product_entity_created = fake_product_repository.get(product_id)
    assert product_entity_created.id == product_id


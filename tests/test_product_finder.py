

import pytest

from tests.repositories import FakeProductRepository
from modules.store.application.find import ProductFinder
from modules.store.application.query import ProductFinderQuery
from modules.store.domain.exceptions import ProductNotExist


def test_product_get_success(product_id, product_entity):
    items = [product_entity]
    product_finder_query = ProductFinderQuery(id=product_id)
    fake_product_repository = FakeProductRepository(items)
    address_finder = ProductFinder(fake_product_repository)
    product = address_finder(product_finder_query)
    assert product.id == product_id


def test_product_get_unsuccess(product_id, ):
    items = []
    product_finder_query = ProductFinderQuery(id=product_id)
    fake_product_repository = FakeProductRepository(items)
    address_finder = ProductFinder(fake_product_repository)

    with pytest.raises(ProductNotExist):
        address_finder(product_finder_query)


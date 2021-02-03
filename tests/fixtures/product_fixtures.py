


import pytest


from modules.store.domain.entity import Product as ProductEntity


@pytest.fixture
def product_id():
    """
    Product id
    @return: product_id
    @rtype: str
    """
    product_id = "b127328b-f0dd-47d8-bcaa-68e57e92159d"
    return product_id


@pytest.fixture
def product_data(product_id, store_id):
    """
    Gets product data
    @param product_id: Product id
    @type product_id: str
    @param store_id: Store id
    @type store_id: str
    @return: product data
    @rtype: dict
    """
    product_data = dict(
        id=product_id,
        name="product_1",
        price=99.99,
        sku="sku1",
        store_id=store_id
    )
    return product_data


@pytest.fixture
def product_entity(product_data):
    """
    Gets product entity
    @param product_data: Product data
    @type product_data: dict
    @return: Product entity
    @rtype: ProductEntity
    """
    product_entity = ProductEntity(**product_data)
    return product_entity


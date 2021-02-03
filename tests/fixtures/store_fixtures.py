


import pytest


from modules.store.domain.entity import Store as StoreEntity


@pytest.fixture
def store_id():
    """
    Store id
    @return: store_id
    @rtype: str
    """
    store_id = "11579097-3ba9-44a2-b59b-844dc7dc6d07"
    return store_id


@pytest.fixture
def store_data(store_id):
    """
    Store data
    @param store_id: store_id
    @type store_id: str
    @return: store data
    @rtype: dict
    """
    store_data = dict(
        id=store_id,
        name="Store fake"
    )
    return store_data


@pytest.fixture
def store_entity(store_data):
    """
    Gets store entity
    @param store_data: store_data
    @type store_data: dict
    @return: Store entity
    @rtype: StoreEntity
    """
    store_entity = StoreEntity(**store_data)
    return store_entity


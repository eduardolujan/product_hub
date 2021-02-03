

import pytest

from modules.store.domain.entity import Address as AddressEntity

@pytest.fixture
def address_id():
    """
    Gets address id
    @return: address_id
    @rtype: str
    """
    address_id = "b127328b-f0dd-47d8-bcaa-68e57e92159d"
    return address_id


@pytest.fixture(autouse=True)
def address_data(address_id, store_id):
    """
    Address data
    @param address_id: fixture address_id
    @type address_id: str
    @return: address data
    @rtype: dict
    """
    address_data = dict(
        id=address_id,
        street="Madero",
        external_number="1000",
        internal_number="",
        city="Morelia",
        state="Michoacan",
        country="MX",
        zipcode="58000",
        store_id=store_id
    )
    return address_data


@pytest.fixture
def address_entity(address_data):
    """
    Address entoty
    @param address_data: Address data
    @type address_data: dict
    @return: Address entity
    @rtype: AddressEntity
    """
    store_entity = AddressEntity(**address_data)
    return store_entity



from modules.store.domain.entity import Address


class AddressCreator:
    """
    Address Creator
    """

    @staticmethod
    def create(id: str = None,
               street: str = None,
               external_number: str = None,
               internal_number: str = None,
               city: str = None,
               state: str = None,
               country: str = None,
               zipcode: str = None,
               store_id: str = None):
        """
        Create address
        """

        address = Address(
            id=id,
            street=street,
            external_number=external_number,
            internal_number=internal_number,
            city=city,
            state=state,
            country=country,
            zipcode=zipcode,
            store_id=store_id
        )
        return address


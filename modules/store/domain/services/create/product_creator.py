

from modules.store.domain.entity import Product


class ProductCreator:
    """
    Product Creator
    """

    @staticmethod
    def create(id: str = None,
               name: str = None,
               price: float = None,
               sku: str = None,
               store_id: str = None):
        """
        Create store
        """
        product = Product(
            id=id,
            name=name,
            price=price,
            sku=sku,
            store_id=store_id)
        return product


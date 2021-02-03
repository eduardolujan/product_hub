
from modules.store.domain.entity import Store


class StoreCreator:
    """
    Store Creator
    """

    @staticmethod
    def create_store(id: str = None,
                     name: str = None):
        """
        Create store
        """
        store = Store(id=id,
                      name=name)
        return store


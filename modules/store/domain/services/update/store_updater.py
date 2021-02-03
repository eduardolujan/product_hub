
from modules.store.domain.entity import UpdateStore


class StoreUpdater:
    """
    Store Creator
    """

    @staticmethod
    def create_store(name: str = None):
        """
        Create store
        """
        update_store = UpdateStore(name=name)
        return update_store


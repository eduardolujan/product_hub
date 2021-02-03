

class AddressNotExist(Exception):
    """
    Address not exists
    """
    def __init__(self, message: str):
        super(AddressNotExist, self).__init__(message)


class AddressAlreadyExists(Exception):
    """
    Store already exists
    """
    def __init__(self, message: str):
        super(AddressAlreadyExists, self).__init__(message)




from .http_error import HttpError
from modules.shared.infrastructure.http import status as http_status


class StoreNotExist(HttpError):
    """
    Store not exists
    """
    def __init__(self,
                 message: str,
                 http_status=http_status.HTTP_404_NOT_FOUND):
        """
        Store not exists
        @param message: message
        @type message: str
        @param http_status: http
        @type http_status:
        """
        super(StoreNotExist, self).__init__(message, http_status=http_status)


class StoreAlreadyExists(HttpError):
    """
    Store already exists
    """

    def __init__(self,
                 message: str,
                 http_status=http_status.HTTP_404_NOT_FOUND):
        super(StoreAlreadyExists, self).__init__(message, http_status=http_status)

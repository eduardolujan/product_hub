
# -*- coding: utf-8 -*-


from .http_error import HttpError
from modules.shared.infrastructure.http import status as http_status


class ProductNotExist(HttpError):
    """
    Product not exists
    """
    def __init__(self,
                 message: str,
                 http_status=http_status.HTTP_404_NOT_FOUND):
        """
        Constructor product not exists
        @param message: message
        @type message: str
        @param http_status: http status
        @type http_status: int
        """
        super(ProductNotExist, self).__init__(message, http_status=http_status)


class ProductAlreadyExists(HttpError):
    """
    Product already exists
    """

    def __init__(self,
                 message: str,
                 http_status=http_status.HTTP_409_CONFLICT):
        """
        Constructor product already exists
        @param message: message
        @type message: str
        @param http_status: http status
        @type http_status: int
        """
        super(ProductAlreadyExists, self).__init__(message, http_status=http_status)

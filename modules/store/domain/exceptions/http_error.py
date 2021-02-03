

# -*- coding: utf-8 -*-


from modules.shared.infrastructure.http import status as http_status


class HttpError(Exception):
    """
    Http error
    """
    def __init__(self,
                 message,
                 http_status=http_status.HTTP_500_INTERNAL_SERVER_ERROR):
        """
        Http error
        @param message: message
        @type message: str
        @param http_status: http status
        @type http_status: str
        """
        super(HttpError, self).__init__(message)
        self.__http_status = http_status

    @property
    def http_status(self):
        """
        Http status
        @return: http status
        @rtype: str
        """
        return self.__http_status

    @http_status.setter
    def setter_http_status(self, value):
        """
        Setter http status
        """
        raise Exception(f"You can't assign http_status the variable directly")


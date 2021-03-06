
from product_hub import get_env
# Domain
from modules.shared.domain.environ import Environ as AbstractEnviron


class PyEnviron(AbstractEnviron):
    """
    Environ
    """

    def __init__(self, environ=None):
        """
        Constructor
        @param environ:
        @type environ:
        """
        self.__environ = environ or get_env()

    def __call__(self, key, default=None):
        return self.__environ(key, default=default)

    def get(self, key, default=None):
        """
        Get str value
        @return: str
        @rtype: str
        """
        return self.__environ(key, default=default)

    def get_str(self, key, default=None):
        """
        Get str value
        @return: str
        @rtype: str
        """
        return self.__environ.str(key, default=default)

    def get_int(self, key, default=None):
        """
        Get int value
        @return: int
        @rtype: int
        """
        return self.__environ.int(key, default=default)

    def get_float(self, key, default=None):
        """
        Get int value
        @return: int
        @rtype: int
        """
        return self.__environ.float(key, default=default)

    def get_list(self, key, default=list()):
        """
        Get int value
        @return: int
        @rtype: int
        """
        return self.__environ.list(key, default=default)

    def get_tuple(self, key, default=tuple()):
        """
        Get tuple value
        @return: tuple
        @rtype: tuple
        """
        return self.__environ.tuple(key, default=default)

    def read_env(self, path):
        """

        """
        self.__environ.read_env(path)



# -*- coding: utf-8 -*-


from sqlalchemy import create_engine

from modules.shared.infrastructure.environ import PyEnviron


class EngineManager:
    """
    Engine manager
    """

    def __init__(self, environ=None, echo=False, logging_name=__name__):
        self.__environ = environ or PyEnviron()
        self.__echo = echo
        self.__logging_name = logging_name
        self.__engine = None

    def get_engine(self):
        """
        Get engine
        @return: engine
        @rtype: engine
        """
        if not self.__engine:
            database_uri = self.__environ('DATABASE_URI')
            self.__engine = create_engine(database_uri,
                                          echo=self.__echo,
                                          logging_name=self.__logging_name)
        return self.__engine


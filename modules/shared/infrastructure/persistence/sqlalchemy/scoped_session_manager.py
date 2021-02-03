
# -*- coding: utf-8 -*-


from sqlalchemy.orm import sessionmaker, scoped_session

from .engine_manager import EngineManager


class ScopedSessionManager:
    """
    Create session()
    """
    def __init__(self,
                 autocommit=False,
                 autoflush=False,
                 engine_manager=None):

        self.__engine_manager = engine_manager or EngineManager()
        self.__autocommit = autocommit
        self.__autoflush = autoflush
        self.__session = None

    def get_session(self):
        """
        Get session
        @return: session
        @rtype: session
        """
        if not self.__session:
            engine = self.__engine_manager.get_engine()
            session_maker = sessionmaker(bind=engine,
                                         autoflush=self.__autoflush,
                                         autocommit=self.__autocommit)
            self.__session = scoped_session(session_maker)
        return self.__session


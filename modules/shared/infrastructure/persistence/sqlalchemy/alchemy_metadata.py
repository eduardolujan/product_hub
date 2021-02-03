


from sqlalchemy.ext.declarative import declarative_base

from .engine_manager import EngineManager

engine = EngineManager().get_engine()

Base = declarative_base(bind=engine)

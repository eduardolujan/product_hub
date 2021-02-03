from logging.config import fileConfig


import os
import sys
import pathlib

import environ
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

parent_dir = os.path.abspath(os.getcwd())
sys.path.append(parent_dir)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

from modules.shared.infrastructure.persistence.sqlalchemy import Base

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from schemas.models import *
target_metadata = [Base.metadata]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_env():
    """
    Get env
    """
    current_path = os.path.dirname(os.path.abspath(__file__))
    project_path = pathlib.Path(current_path).parent
    env = environ.Env()
    if os.path.exists(str(project_path)):
        env_path = os.path.join(project_path, '.env')
        env.read_env(env_path)
    return env


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # url = config.get_main_option("sqlalchemy.url")
    env = get_env()
    url = env('DATABASE_URI')
    context.config.set_main_option('sqlalchemy.url', url)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    env = get_env()
    url = env('DATABASE_URI')
    config_section = config.get_section(config.config_ini_section)
    config_section["sqlalchemy.url"] = url
    connectable = engine_from_config(
        config_section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
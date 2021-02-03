"""Sqlalchemy Store model
"""


# -*- coding: utf-8 -*-


import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import mapper

from modules.shared.infrastructure.persistence.sqlalchemy import Base
from modules.store.domain.entity import Store as StoreEntity


Store = sa.Table(
    'store',
    Base.metadata,
    sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
    sa.Column('name', sa.String, nullable=False, default=""),
)


mapper(StoreEntity, Store)




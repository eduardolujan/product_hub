


import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship, mapper

from modules.shared.infrastructure.persistence.sqlalchemy import Base
from modules.store.domain.entity import Product as ProductEntity


Product = sa.Table(
    'product',
    Base.metadata,
    sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
    sa.Column('name', sa.String, nullable=False, default=""),
    sa.Column('price', sa.Float, nullable=False, default=0.0),
    sa.Column('sku', sa.String, nullable=False, default=""),
    sa.Column('store_id', sa.ForeignKey('store.id', deferrable=True, initially='DEFERRED'), index=True),
)

mapper(ProductEntity, Product)


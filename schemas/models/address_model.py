

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship, mapper


from modules.shared.infrastructure.persistence.sqlalchemy import Base
from modules.store.domain.entity import Address as AddressEntity


Address = sa.Table(
    'address',
    Base.metadata,
    sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
    sa.Column('street', sa.String, nullable=False, default=""),
    sa.Column('external_number', sa.String, nullable=False, default=""),
    sa.Column('internal_number', sa.String, nullable=False, default=""),
    sa.Column('city', sa.String, nullable=False, default=""),
    sa.Column('state', sa.String, nullable=False, default=""),
    sa.Column('country', sa.String, nullable=False, default=""),
    sa.Column('zipcode', sa.String, nullable=False, default=""),
    sa.Column('store_id', sa.ForeignKey('store.id', deferrable=True, initially='DEFERRED'), index=True),
)

mapper(AddressEntity, Address)

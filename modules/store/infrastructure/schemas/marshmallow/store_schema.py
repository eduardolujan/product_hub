

from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemySchema

from schemas.models import Store


class StoreSchema(SQLAlchemySchema):
    """
    Store Schema
    """

    id = fields.String(required=True)
    name = fields.String(required=True)

    class Meta:
        """
        Class meta
        """
        model = Store
        load_instance = True
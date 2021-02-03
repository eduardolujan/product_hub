

from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from schemas.models import Address


class AddressSchema(SQLAlchemySchema):
    """
    Address Schema
    """

    id = fields.String(required=True)
    street = fields.String(required=True)
    external_number = fields.String(required=True)
    internal_number = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    country = fields.String(required=True)
    zipcode = fields.String(required=True)
    store_id = fields.String(required=True)

    class Meta:
        """
        Class meta
        """
        model = Address
        load_instance = True
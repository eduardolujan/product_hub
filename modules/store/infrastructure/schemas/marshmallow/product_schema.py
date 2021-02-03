

from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemySchema


class ProductSchema(Schema):
    """
    Product Schema
    """

    id = fields.String(required=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    sku = fields.String(required=True)
    store_id = fields.String(required=True)



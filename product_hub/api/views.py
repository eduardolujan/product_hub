
from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from product_hub.api import resources
from modules.shared.infrastructure.log import get_logger

log = get_logger(__file__)

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(resources.ProductResource, "/products/<string:product_id>", endpoint="product")
api.add_resource(resources.ProductListResource, "/products", endpoint="products")
api.add_resource(resources.StoreResource, "/stores/<string:store_id>", endpoint="store")
api.add_resource(resources.StoreListResource, "/stores", endpoint="stores")
api.add_resource(resources.AddressesResource, "/address/<string:address_id>", endpoint="address")
api.add_resource(resources.AddressListResource, "/address", endpoint="addresses")


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(err):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    log.exception(err)
    return jsonify(err.messages), 400

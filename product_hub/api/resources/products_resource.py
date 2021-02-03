


import json

from flask import request
from flask_restful import Resource

from modules.store.infrastructure.tasks import celery as celery_tasks
from modules.store.infrastructure.schemas.marshmallow import ProductSchema
from modules.store.infrastructure.repository.sqlalchemy import ProductRepository
from modules.shared.infrastructure.http import status
from modules.shared.infrastructure.log import get_logger
from modules.store.application.query import ProductFinderQuery
from modules.store.application.find import ProductFinder


log = get_logger(__file__)


class ProductResource(Resource):
    """
    Product Resource
    """
    def get(self, product_id):
        product_finder_query = ProductFinderQuery(
            id=product_id
        )
        product_repository = ProductRepository()
        store_finder = ProductFinder(product_repository)
        store = store_finder(product_finder_query)
        product_schema = ProductSchema()
        product_dumped = product_schema.dump(store)
        response_data = dict(
            data=product_dumped
        )
        return response_data, 200


class ProductListResource(Resource):
    """
    Product List Resource
    """

    def post(self):
        """
        Get resorce
        """
        try:
            request_data = request.json
            celery_tasks.ProductCreateCeleryHandler().delay(request_data)

            response_data = dict(
                message=f"Created product id: {request_data.get('id')}",
                success=True
            )
            return response_data, status.HTTP_201_CREATED

        except Exception as err:
            log.exception(f"Error in ProductListResource::post, err:{err}")
            response_data = dict(
                message=f"{err}",
                success=True
            )
            return response_data, status.HTTP_500_INTERNAL_SERVER_ERROR


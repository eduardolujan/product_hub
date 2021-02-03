from flask import request
from flask_restful import Resource


from modules.store.infrastructure.schemas.marshmallow import StoreSchema
from modules.store.infrastructure.repository.sqlalchemy import StoreRepository
from modules.shared.infrastructure.http import status as http_status
from modules.shared.infrastructure.log import get_logger
from modules.store.application.command.create import StoreCreateCommand
from modules.store.application.command.update import StoreUpdateCommand
from modules.store.application.query import StoreFinderQuery
from modules.store.application.create import StoreCreator
from modules.store.application.update import StoreUpdater
from modules.store.application.find import StoreFinder
from modules.store.application.searcher import StoreSearcher


log = get_logger(__file__)


class StoreResource(Resource):
    """
    Store Resource
    """
    def get(self, store_id):
        try:
            store_finder_query = StoreFinderQuery(
                id=store_id
            )
            store_repository = StoreRepository()
            store_finder = StoreFinder(store_repository)
            store = store_finder(store_finder_query)
            store_schema = StoreSchema()
            store_dumped = store_schema.dump(store)
            response_data = dict(
                data=store_dumped
            )
            return response_data, http_status.HTTP_200_OK

        except Exception as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                data=dict()
            )
            return response_data, http_status.HTTP_500_INTERNAL_SERVER_ERROR

    def patch(self, store_id):
        try:
            request_data = request.json
            store_update_command = StoreUpdateCommand(
                name=request_data.get('name')
            )
            store_repository = StoreRepository()
            store_updater = StoreUpdater(store_repository)
            store = store_updater(store_id, store_update_command)
            store_schema = StoreSchema()
            store_dumped = store_schema.dump(store)
            response_data = dict(
                message=f"Updated {store_id}"
            )
            return response_data, http_status.HTTP_200_OK
        except Exception as err:
            log.exception(f"Error StoreResource::patch, err:{err}")

            _http_status = http_status.HTTP_500_INTERNAL_SERVER_ERROR
            if hasattr(err.http_status):
                _http_status = err.http_status

            response_data = dict(
                success=False,
                message=f"{err}"
            )
            return response_data, _http_status

    def delete(self, store_id):
        try:
            request_data = request.json
            store_update_command = StoreUpdateCommand(
                name=request_data.get('name')
            )
            store_repository = StoreRepository()
            store_updater = StoreUpdater(store_repository)
            store = store_updater(store_id, store_update_command)
            store_schema = StoreSchema()
            response_data = dict(
                message=f"Updated {store_id}"
            )
            return response_data, http_status.HTTP_200_OK


        except Exception as err:
            log.exception(f"Error StoreResource::patch, err:{err}")
            _http_status = http_status.HTTP_500_INTERNAL_SERVER_ERROR
            if hasattr(err.http_status):
                _http_status = err.http_status

            response_data = dict(
                success=False,
                message=f"{err}",
                data=dict()
            )
            return response_data, http_status.HTTP_201_CREATED


class StoreListResource(Resource):
    """
    Store List Resource
    """
    def get(self):
        """
        Searcher store
        """
        try:
            store_repository = StoreRepository()
            store_searcher = StoreSearcher(store_repository)
            stores = store_searcher()
            store_schema = StoreSchema()
            store_dumped = store_schema.dump(stores, many=True)
            response_data = dict(
                message=f"Ok",
                success=True,
                data=store_dumped
            )
            return response_data, http_status.HTTP_200_OK
        except Exception as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                data=dict()
            )
            return response_data, http_status.HTTP_201_CREATED

    def post(self):
        """
        Create store
        """
        try:
            request_data = request.json
            store_create_command = StoreCreateCommand(
                id=request_data.get('id'),
                name=request_data.get('name')
            )
            store_repository = StoreRepository()
            store_creator = StoreCreator(store_repository)
            store_creator(store_create_command)
            response_data = dict(
                message=f"Created store {request_data.get('id')}",
                success=True)
            return response_data, http_status.HTTP_200_OK
        except Exception as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                data=dict()
            )
            return response_data, http_status.HTTP_201_CREATED




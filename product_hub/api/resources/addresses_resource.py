
# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource

from modules.store.infrastructure.schemas.marshmallow import AddressSchema
from modules.store.infrastructure.repository.sqlalchemy import AddressRepository, StoreRepository
from modules.shared.infrastructure.log import get_logger
from modules.shared.infrastructure.http import status
from modules.store.application.command.create import AddressCreateCommand
from modules.store.application.query import AddressFinderQuery
from modules.store.application.create import AddressCreator
from modules.store.application.find import AddressFinder

log = get_logger(__file__)


class AddressesResource(Resource):
    """
    Store Resource
    """
    def get(self, address_id):
        """
        Get
        """
        try:
            address_get_command = AddressFinderQuery(
                id=address_id
            )
            address_repository = AddressRepository()
            address_finder = AddressFinder(address_repository)
            address = address_finder(address_get_command)
            address_schema = AddressSchema()
            address_dumped = address_schema.dump(address)
            response_data = dict(
                data=address_dumped
            )
            return response_data, status.HTTP_200_OK
        except Exception as err:
            log.exception(err)
            response_data = dict(
                success=True,
                message=f"{err}"
            )
            return response_data, status.HTTP_500_INTERNAL_SERVER_ERROR


class AddressListResource(Resource):
    """
    Address List Resource
    """

    def post(self):
        """
        Get resource
        """
        try:
            request_data = request.json
            store_create_command = AddressCreateCommand(
                id=request_data.get('id'),
                street=request_data.get('street'),
                external_number=request_data.get('external_number'),
                internal_number=request_data.get('internal_number'),
                city=request_data.get('city'),
                state=request_data.get('state'),
                country=request_data.get('country'),
                zipcode=request_data.get('zipcode'),
                store_id=request_data.get('store_id')
            )
            address_repository = AddressRepository()
            store_repository = StoreRepository()
            address_creator = AddressCreator(address_repository, store_repository)
            address_creator(store_create_command)
            response_data = dict(
                success=True,
                message=f"Address created {request_data.get('id')}"
            )
            return response_data, status.HTTP_201_CREATED

        except Exception as err:
            log.exception(err)
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            return response_data, status.HTTP_500_INTERNAL_SERVER_ERROR


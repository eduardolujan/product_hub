


from celery import Task, task
from celery.utils.log import get_task_logger

from modules.shared.infrastructure.persistence.sqlalchemy import SessionManager, ScopedSessionManager
from modules.store.infrastructure.repository.sqlalchemy import ProductRepository, StoreRepository
from modules.store.application.create import ProductCreator
from modules.store.application.command.create import ProductCreateCommand


log = get_task_logger(__name__)


class ProductCreateCeleryHandler(Task):
    """
    Product create celery handler
    """

    name = "product_create_celery_handler"

    def run(self, *args, **kwargs):
        create_product_command = args[0]
        session_manager = SessionManager()
        product_create_command = ProductCreateCommand(
            id=create_product_command.get('id'),
            name=create_product_command.get('name'),
            price=create_product_command.get('price'),
            sku=create_product_command.get('sku'),
            store_id=create_product_command.get('store_id')
        )
        product_repository = ProductRepository(session_manager=session_manager)
        store_repository = StoreRepository(session_manager=session_manager)
        product_creator = ProductCreator(product_repository, store_repository)
        product_creator(product_create_command)
        print(f"Finished product {create_product_command.get('id')}")

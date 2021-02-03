import os
import sys
import pathlib

from flask import Flask
from product_hub import api
from celery import Celery


def create_app(testing=False):
    """Application factory, used to create application"""
    app = Flask("product_hub")
    app.config.from_object("product_hub.config")
    celery = make_celery(app)

    if testing is True:
        app.config["TESTING"] = True

    register_blueprints(app)
    register_celery_tasks(celery)
    return app, celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(api.views.blueprint)


def register_celery_tasks(celery):
    from modules.store.infrastructure.tasks.celery import ProductCreateCeleryHandler
    celery.tasks.register(ProductCreateCeleryHandler())

"""Default configuration

Use env var to override
"""
import os
import pathlib

from environ import Env

env = Env()

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = pathlib.Path(CURRENT_PATH).parent

ENV_PATH = os.path.join(ROOT_PATH, '.env')
if os.path.exists(ENV_PATH):
    env.read_env(ENV_PATH)

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
# CELERY = {
#     "broker_url": os.getenv("CELERY_BROKER_URL"),
#     "result_backend": os.getenv("CELERY_RESULT_BACKEND_URL"),
# }
#
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

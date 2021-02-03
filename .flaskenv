FLASK_ENV=development
FLASK_APP=product_hub.app:create_app
SECRET_KEY=changeme
DATABASE_URI=sqlite:////tmp/product_hub.db
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=rpc://


amqp://rabbitmq:password@localhost:5672/vhost


redis://localhost:6379/0

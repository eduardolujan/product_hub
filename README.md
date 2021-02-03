# Product HUB 
## Ports and adapters
Project based in port and adapters aka `Hexagonal Architecture`
## Setup
### Enviroment file 

```bash
$ cd product_hub
$ cat <<EOT >> .env
# Flask
# ------------------------------------------------------------------------------
FLASK_APP_HOST=product_hub_flask
FLASK_APP=app:app
SECRET_KEY=7dJghTRxWVYtupHYB722YbZkXpFJMM7jsERekzt2tMQwcwatncgt5As69txNxR3s
DATABASE_URI=postgresql+psycopg2://postgres:password@product_hub_postgres:5432/product_hub


# Celery
# ------------------------------------------------------------------------------

CELERY_HOST=product_hub_celery
CELERY_BROKER_URL=amqp://rabbitmq:password@product_hub_rabbitmq:5672/app
CELERY_RESULT_BACKEND=redis://product_hub_redis:6379


# PostgreSQL
# ------------------------------------------------------------------------------
POSTGRES_HOST=product_hub_postgres
POSTGRES_PORT=5432
POSTGRES_DB=product_hub
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DATA=~/Documents/Projects/docker/product_hub/postgres
POSTGRES_BACKUPS=~/Documents/projects/docker/product_hub/postgres_backups
POSTGRES_EXTERNAL_PORT=5432
POSTGRES_HOST_LOCAL=127.0.0.1


# Redis
# ------------------------------------------------------------------------------
REDIS_PORT=6379
REDIS_HOST=product_hub_redis
REDIS_HOST_LOCAL=localhost
REDIS_DATA=~/Documents/projects/docker/product_hub/redis


# Rabbitmq
# ------------------------------------------------------------------------------
RABBITMQ_HOST=product_hub_rabbitmq
RABBITMQ_HOST_LOCAL=localhost
RABBITMQ_USER=rabbitmq
RABBITMQ_PASS=password
RABBITMQ_VHOST=app
RABBITMQ_MANAGEMENT_PORT=15672
RABBITMQ_PORT=5672
RABBITMQ_DIR=~/Documents/projects/docker/product_hub/rabbitmq

EOT
```


## Docker compose
```bash
$ docker-compose up -d && docker-compose logs -f

```

## Update db
```bash
$ docker exec -ti product_hub_app alembic upgrade head
```
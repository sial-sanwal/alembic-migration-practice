# Install
- poetry add alembic
- poetry add psycopg2-binary

## new-project setup
- poetry run alembic init [projetname]
- change or set the db_url in the sqlalchemy.url in alembic.ini
- create the sqlalchemy model for your table
- change target metadatain of your table in  env file of alembic
- every change in models run in the following command
- poetry run alembic revision --autogenerate -m "create the todo table"
- poetry run alembic upgrade head
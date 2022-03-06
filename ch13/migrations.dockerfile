FROM python:3.9-slim

RUN mkdir -p /orders/orders

WORKDIR /orders

RUN pip install -U pip && pip install pipenv

COPY Pipfile Pipfile.lock /orders/

RUN pipenv install --dev --system --deploy

COPY orders/orders_service /orders/orders/orders_service/
COPY orders/repository /orders/orders/repository/
COPY orders/web /orders/orders/web/
COPY migrations /orders/migrations
COPY alembic.ini /orders/alembic.ini

EXPOSE 8000

ENV PYTHONPATH=/orders

CMD ["alembic", "upgrade", "heads"]

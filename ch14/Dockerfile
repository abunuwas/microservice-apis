FROM python:3.9-slim

RUN mkdir -p /orders/orders

WORKDIR /orders

RUN pip install -U pip && pip install pipenv

COPY Pipfile Pipfile.lock /orders/

RUN pipenv install --system --deploy

COPY orders/orders_service /orders/orders/orders_service/
COPY orders/repository /orders/orders/repository/
COPY orders/web /orders/orders/web/
COPY oas.yaml /orders/oas.yaml
COPY public_key.pem /orders/public_key.pem
COPY private.pem /orders/private.pem

EXPOSE 8000

CMD ["uvicorn", "orders.web.app:app", "--host", "0.0.0.0"]

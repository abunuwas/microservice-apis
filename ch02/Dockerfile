FROM python:3.8-slim

RUN mkdir -p /orders/orders

WORKDIR /orders

RUN pip install -U pip && pip install pipenv

COPY Pipfile Pipfile.lock /orders/

RUN pipenv install --system --ignore-pipfile

COPY orders /orders/orders

EXPOSE 8000

CMD ["uvicorn", "orders.app:app", "--host", "0.0.0.0"]

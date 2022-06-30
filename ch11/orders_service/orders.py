import requests

from orders.orders_service.exceptions import APIIntegrationError, InvalidActionError


class OrderItem:
    def __init__(self, id, product, quantity, size):
        self.id = id
        self.product = product
        self.quantity = quantity
        self.size = size

    def dict(self):
        return {"product": self.product, "size": self.size, "quantity": self.quantity}


class Order:
    def __init__(
        self,
        id,
        created,
        items,
        status,
        schedule_id=None,
        delivery_id=None,
        order_=None,
    ):
        self._order = order_
        self._id = id
        self._created = created
        self.items = [OrderItem(**item) for item in items]
        self._status = status
        self.schedule_id = schedule_id
        self.delivery_id = delivery_id

    @property
    def id(self):
        return self._id or self._order.id

    @property
    def created(self):
        return self._created or self._order.created

    @property
    def status(self):
        return self._status or self._order.status

    def cancel(self):
        if self.status == "progress":
            response = requests.post(
                f"http://localhost:3000/kitchen/schedules/{self.schedule_id}/cancel",
                json={"order": [item.dict() for item in self.items]},
            )
            if response.status_code == 200:
                return
            raise APIIntegrationError(f"Could not cancel order with id {self.id}")
        if self.status == "delivery":
            raise InvalidActionError(f"Cannot cancel order with id {self.id}")

    def pay(self):
        response = requests.post(
            "http://localhost:3001/payments", json={"order_id": self.id}
        )
        if response.status_code == 201:
            return
        raise APIIntegrationError(
            f"Could not process payment for order with id {self.id}"
        )

    def schedule(self):
        response = requests.post(
            "http://localhost:3000/kitchen/schedules",
            json={"order": [item.dict() for item in self.items]},
        )
        if response.status_code == 201:
            return response.json()["id"]
        raise APIIntegrationError(f"Could not schedule order with id {self.id}")

    def dict(self):
        return {
            "id": self.id,
            "order": [item.dict() for item in self.items],
            "status": self.status,
            "created": self.created,
        }

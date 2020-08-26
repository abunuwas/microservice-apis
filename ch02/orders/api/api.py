from typing import List
from uuid import UUID

from fastapi import HTTPException
from starlette import status

from orders.app import app
from orders.orders.orders import OrdersCollection, Order
from orders.api.schemas import GetOrderSchema, CreateOrderSchema

orders_collection = OrdersCollection()


@app.get('/orders', response_model=List[GetOrderSchema])
def get_orders():
    return [
        order.dict() for order in orders_collection.to_list()
    ]


@app.post('/orders', status_code=status.HTTP_201_CREATED, response_model=GetOrderSchema)
def create_order(order_details: CreateOrderSchema):
    order = Order(order_details.order, orders_collection).create()
    return order.dict()


@app.get('/orders/{order_id}', response_model=GetOrderSchema)
def get_order(order_id: UUID):
    order = orders_collection.get(order_id)
    if order is None:
        raise HTTPException(
            status_code=404, detail=f'Order with ID {order_id} not found'
        )
    return order


@app.put('/orders/{order_id}', response_model=GetOrderSchema)
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    order = orders_collection.get(order_id)
    if order is None:
        raise HTTPException(
            status_code=404, detail=f'Order with ID {order_id} not found'
        )
    return order.update(order_details).dict()


@app.delete('/orders/{order_id}', response_model=GetOrderSchema)
def delete_order(order_id: UUID):
    order = orders_collection.get(order_id)
    if order is None:
        raise HTTPException(
            status_code=404, detail=f'Order with ID {order_id} not found'
        )
    order.delete()


@app.post('/orders/{order_id}/cancel', response_model=GetOrderSchema)
def cancel_order(order_id: UUID):
    order = orders_collection.get(order_id)
    if order is None:
        raise HTTPException(
            status_code=404, detail=f'Order with ID {order_id} not found'
        )
    return order.cancel().dict()


@app.post('/orders/{order_id}/pay', response_model=GetOrderSchema)
def pay_order(order_id: UUID):
    order = orders_collection.get(order_id)
    if order is None:
        raise HTTPException(
            status_code=404, detail=f'Order with ID {order_id} not found'
        )
    return order.pay().dict()

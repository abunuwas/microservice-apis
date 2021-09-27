from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, conint


class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'


class StatusEnum(Enum):
    created = 'created'
    paid = 'paid'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'


class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[conint(ge=1, strict=True)] = 1


class CreateOrderSchema(BaseModel):
    order: List[OrderItemSchema]


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: StatusEnum


class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]

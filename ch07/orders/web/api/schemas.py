from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, Extra, conint


class Size(str, Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'


class Status(str, Enum):
    created = 'created'
    paid = 'paid'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'


class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[conint(ge=1)] = 1

    class Config:
        extra = Extra.forbid


class CreateOrderSchema(BaseModel):
    order: List[OrderItemSchema]

    class Config:
        extra = Extra.forbid


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: Status

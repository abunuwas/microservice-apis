from enum import Enum

from pydantic import BaseModel, Field


class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'


class Something(BaseModel):
    name: str
    flavour: str = Field(description='the flavour you want')
    size: Size


coffee = Something(name='coffee', size='small')

print(coffee)

print(Something.schema_json(indent=2))

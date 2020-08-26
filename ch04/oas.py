from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields, validate

specification = APISpec(
    title='Orders API',
    version='1.0.0',
    openapi_version='3.0.3',
    plugins=[MarshmallowPlugin()],
    **{
        'info': {
            'description': 'API that allows you to manage orders for CoffeeMesh'
        },
        'servers': [
            {
                'url': 'https://coffeemesh.com',
                'description': 'main production server'
            },
            {
                'url': 'https://coffeemesh-staging.com',
                'description': 'staging server for testing purposes only'
            }
        ]
    }
)


class OrderItemSchema(Schema):
    product = fields.String(required=True)
    size = fields.String(
        required=True, validate=validate.OneOf(['small', 'medium', 'big'])
    )
    quantity = fields.Integer(
        validate=validate.Range(1, min_inclusive=True), default=1, doc_default=1
    )


class CreateOrderSchema(Schema):
    order = fields.List(fields.Nested(OrderItemSchema), required=True)


class GetOrderSchema(Schema):
    id = fields.UUID(required=True)
    created = fields.Integer(required=True, description='Date in the form of UNIX timestmap')
    status = fields.String(
        required=True, validate=validate.OneOf(['active', 'cancelled', 'completed'])
    )
    order = fields.List(fields.Nested(OrderItemSchema), required=True)


specification.components.schema('OrderItemSchema', schema=OrderItemSchema)
specification.components.schema('GetOrderSchema', schema=GetOrderSchema)
specification.components.schema('CreateOrderSchema', schema=CreateOrderSchema)

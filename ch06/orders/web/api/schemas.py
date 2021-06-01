from marshmallow import Schema, fields, validate, EXCLUDE


class OrderItemSchema(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    product = fields.String(required=True)
    size = fields.String(
        required=True, validate=validate.OneOf(['small', 'medium', 'big'])
    )
    quantity = fields.Integer(
        validate=validate.Range(1, min_inclusive=True), default=1, example=1
    )


class CreateOrderSchema(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    order = fields.List(fields.Nested(OrderItemSchema), required=True)


class GetOrderSchema(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    id = fields.UUID(required=True)
    created = fields.Integer(
        required=True, description='Date in the form of UNIX timestmap'
    )
    status = fields.String(
        required=True,
        validate=validate.OneOf(['active', 'cancelled', 'completed'])
    )
    order = fields.List(fields.Nested(OrderItemSchema), required=True)

from marshmallow import Schema, fields, validate, EXCLUDE


class OrderItemSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    product = fields.String(required=True)
    size = fields.String(
        required=True, validate=validate.OneOf(['small', 'medium', 'big'])
    )
    quantity = fields.Integer(
        validate=validate.Range(1, min_inclusive=True), required=True,
    )


class ScheduleOrderSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    order = fields.List(fields.Nested(OrderItemSchema), required=True)


class GetScheduledOrderSchema(ScheduleOrderSchema):
    id = fields.UUID(required=True)
    scheduled = fields.Integer(
        required=True, description='Date in the form of UNIX timestmap'
    )
    status = fields.String(
        required=True,
        validate=validate.OneOf(['pending', 'progress', 'cancelled', 'finished'])  # noqa: E501
    )


class GetKitchenScheduleParameters(Schema):
    progress = fields.Boolean()
    limit = fields.Integer()
    since = fields.DateTime()

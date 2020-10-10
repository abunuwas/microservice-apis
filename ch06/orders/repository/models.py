import datetime

from mongoengine import Document, DateTimeField, StringField, ListField, \
    IntField, EmbeddedDocument, EmbeddedDocumentField, UUIDField


class OrderItem(EmbeddedDocument):
    product = StringField(required=True)
    quantity = IntField(required=True)
    size = StringField(required=True)


class Order(EmbeddedDocument):
    created = DateTimeField(default=datetime.datetime.utcnow, required=True)
    updated = DateTimeField(default=datetime.datetime.utcnow, required=True)
    products = ListField(EmbeddedDocumentField(OrderItem), required=True)
    order_status = StringField(default='placed', required=True)


class UserOrders(Document):
    id = UUIDField(required=True)
    orders = ListField(EmbeddedDocumentField(Order))

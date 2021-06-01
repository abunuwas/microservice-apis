from flask.views import MethodView
from flask_smorest import Blueprint

from orders.api.schemas import GetOrderSchema, CreateOrderSchema

blueprint = Blueprint(
    'orders', __name__, url_prefix='/', description='Orders API'
)


order = {
    'id': 'asdf',
    'created': '1234',
    'order': [
        {
            'size': 'big'
        }
    ]
}


@blueprint.route('/orders')
class Orders(MethodView):

    # @blueprint.response(GetOrderSchema(many=True))
    def get(self):
        # return [order]
        return {
            'orders': [order]
        }, 200

    # @blueprint.arguments(CreateOrderSchema)
    # @blueprint.response(GetOrderSchema, code=201)
    def post(self, payload):
        return order, 201


@blueprint.route('/order/<uuid:order_id>')
class Order(MethodView):

    # @blueprint.response(GetOrderSchema)
    def get(self, order_id):
        return order, 200

    # @blueprint.arguments(CreateOrderSchema)
    # @blueprint.response(GetOrderSchema)
    def put(self, payload, order_id):
        return order, 200

    # @blueprint.response(code=204)
    def delete(self, order_id):
        return '', 204


@blueprint.route('/order/<uuid:order_id>/cancel')
def cancel_order(order_id):
    return '', 200


@blueprint.route('/order/<uuid:order_id>/pay')
def pay_order(order_id):
    return '', 200

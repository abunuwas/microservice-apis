from datetime import datetime

from ariadne import QueryType

query = QueryType()


@query.field('allProducts')
def resolve_all_products(*_):
    return [
        {
            'id': '9907a09d-611c-4de9-807d-7672337baa3e',
            'name': 'Muffin',
            'price': 10.0,
            'ingredients': [],
            'has_filling': False,
            'has_nuts_topping_option': True,
            'lastUpdated': datetime.now(),
        },
        {
            'id': '1843bdcf-3ea7-484d-91a8-68e985f3cad8',
            'name': 'Cappuccino',
            'price': 10.0,
            'ingredients': [],
            'has_cream_on_top_option': False,
            'has_serve_on_ice_option': True,
            'lastUpdated': datetime.now(),
        }
    ]


@query.field('allIngredients')
def resolve_all_ingredients(*_):
    return [
        {
            'id': '788050e6-8073-47d4-aa2e-32aa70a12dab',
            'name': 'Milk',
            'stock': {
                'amount': 100.0,
                'unit': 'LITERS',
            },
            'products': [],
        }
    ]


@query.field('products')
def resolve_products(*_, input=None):
    products = [
        {
            'id': '9907a09d-611c-4de9-807d-7672337baa3e',
            'name': 'Muffin',
            'price': 10.0,
            'ingredients': [],
            'available': True,
            'has_filling': False,
            'has_nuts_topping_option': True,
        },
        {
            'id': '1843bdcf-3ea7-484d-91a8-68e985f3cad8',
            'name': 'Cappuccino',
            'price': 10.0,
            'ingredients': [],
            'available': False,
            'has_cream_on_top_option': False,
            'has_serve_on_ice_option': True,
        }
    ]
    if input is None:
        return products
    filtered = [
        product for product in products
        if product['available'] is input['available']
    ]
    if input.get('minPrice') is not None:
        filtered = [
            product for product in products
            if product['price'] >= input['minPrice']
        ]
    if input.get('maxPrice') is not None:
        filtered = [
            product for product in products
            if product['price'] <= input['maxPrice']
        ]
    filtered.sort(
        key=lambda product: product[input['sortBy']],
        reverse=input['sort'] == 'DESCENDING'
    )
    return filtered

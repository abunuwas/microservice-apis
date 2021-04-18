import uuid

from ariadne import MutationType

mutation = MutationType()


@mutation.field('addProduct')
def resolve_add_product(*_, name, type, input):
    product = {
        'id': uuid.uuid4(),
        'name': name,
        'available': input.get('available', False),
        'ingredients': input.get('ingredients', []),
    }
    if type == 'cake':
        product.update({
            'has_filling': input['has_filling'],
            'has_nuts_topping_option': input['has_nuts_topping_option'],
        })
    else:
        product.update({
            'has_cream_on_top_option': input['has_cream_on_top_option'],
            'has_serve_on_ice_option': input['has_serve_on_ice_option'],
        })
    return product

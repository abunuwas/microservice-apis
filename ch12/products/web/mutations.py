import uuid
from datetime import datetime

from ariadne import MutationType

from exceptions import ItemNotFoundError
from web.data import products, ingredients, suppliers

mutation = MutationType()


@mutation.field('addSupplier')
def resolve_add_supplier(*_, name, input):
    input['name'] = name
    input['id'] = uuid.uuid4()
    suppliers.append(input)
    return input


@mutation.field('addIngredient')
def resolve_add_ingredient(*_, name, input):
    input['name'] = name
    input['id'] = uuid.uuid4()
    input['lastUpdated'] = datetime.utcnow()
    ingredients.append(input)
    return input


@mutation.field('addProduct')
def resolve_add_product(*_, name, type, input):
    product = {
        'id': uuid.uuid4(),
        'name': name,
        'available': input.get('available', False),
        'ingredients': input.get('ingredients', []),
        'lastUpdated': datetime.utcnow(),
    }
    if type == 'cake':
        product.update({
            'hasFilling': input['hasFilling'],
            'hasNutsToppingOption': input['hasNutsToppingOption'],
        })
    else:
        product.update({
            'hasCreamOnTopOption': input['hasCreamOnTopOption'],
            'hasServeOnIceOption': input['hasServeOnIceOption'],
        })
    products.append(product)
    return product


@mutation.field('updateProduct')
def resolve_update_product(*_, id, input):
    for product in products:
        if product['id'] == id:
            product.update(input)
            product['lastUpdated'] = datetime.utcnow()
            return product
    raise ItemNotFoundError(f'Product with ID {id} not found')


@mutation.field('deleteProduct')
def resolve_delete_product(*_, id):
    for index, product in enumerate(products):
        if product['id'] == id:
            products.pop(index)
            return True
    raise ItemNotFoundError(f'Product with ID {id} not found')


@mutation.field('updateStock')
def resolve_update_stock(*_, id, changeAmount):
    for ingredient in ingredients:
        if ingredient['id'] == id:
            ingredient['stock'] = changeAmount
            return ingredient
    raise ItemNotFoundError(f'Ingredient with ID {id} not found')

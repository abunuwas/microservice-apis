from itertools import islice

from ariadne import QueryType

from exceptions import ItemNotFoundError
from web.data import products, ingredients

query = QueryType()


@query.field('allProducts')
def resolve_all_products(*_):
    return products


@query.field('allIngredients')
def resolve_all_ingredients(*_):
    return ingredients


def get_page(items, items_per_page, page):
    page = page - 1
    start = items_per_page * page if page > 0 else page
    stop = start + items_per_page
    return list(islice(items, start, stop))


@query.field('products')
def resolve_products(*_, input=None):
    filtered = [product for product in products]
    if input is None:
        return filtered
    filtered = [
        product for product in filtered
        if product['available'] is input['available']
    ]
    if input.get('minPrice') is not None:
        filtered = [
            product for product in filtered
            if product['price'] >= input['minPrice']
        ]
    if input.get('maxPrice') is not None:
        filtered = [
            product for product in filtered
            if product['price'] <= input['maxPrice']
        ]
    filtered.sort(
        key=lambda product: product[input['sortBy']],
        reverse=input['sort'] == 'DESCENDING'
    )
    return get_page(filtered, input['resultsPerPage'], input['page'])


@query.field('product')
def resolve_product(*_, id):
    for product in products:
        if product['id'] == id:
            return product
    raise ItemNotFoundError(f'Product with ID {id} not found')


@query.field('ingredient')
def resolve_ingredient(*_, id):
    for ingredient in ingredients:
        if ingredient['id'] == id:
            return ingredient
    raise ItemNotFoundError(f'Ingredient with ID {id} not found')

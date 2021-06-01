from copy import deepcopy

from ariadne import QueryType

from repository import ProductsRepository, IngredientsRepository
from web.data import products, ingredients

query = QueryType()


@query.field('allProducts')
def resolve_all_products(*_):
    # products_with_ingredients = [deepcopy(product) for product in products]
    # for product in products_with_ingredients:
    #     for ingredient_recipe in product['ingredients']:
    #         for ingredient in ingredients:
    #             if ingredient['id'] == ingredient_recipe['ingredient']:
    #                 ingredient_recipe['ingredient'] = ingredient
    # return products_with_ingredients
    return products


@query.field('allIngredients')
def resolve_all_ingredients(*_):
    return IngredientsRepository().list()


@query.field('products')
def resolve_products(*_, input=None):
    return ProductsRepository().filter(input)


@query.field('product')
def resolve_product(*_, id):
    return ProductsRepository().get(id)


@query.field('ingredient')
def resolve_ingredient(*_, id):
    return IngredientsRepository().get(id)

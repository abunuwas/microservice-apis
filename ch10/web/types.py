import copy
from datetime import datetime

from ariadne import UnionType, ScalarType, InterfaceType, ObjectType

from web.data import ingredients, suppliers, products

product_interface = InterfaceType("ProductInterface")
product_type = UnionType("Product")
ingredient_type = ObjectType("Ingredient")
supplier_type = ObjectType("Supplier")

datetime_scalar = ScalarType("Datetime")


@datetime_scalar.serializer
def serialize_datetime_scalar(date):
    return date.isoformat()


@datetime_scalar.value_parser
def parse_datetime_scalar(date):
    return datetime.fromisoformat(date)


@product_type.type_resolver
def resolve_product_type(obj, *_):
    if "hasFilling" in obj:
        return "Cake"
    return "Beverage"


@product_interface.field("ingredients")
def resolve_product_ingredients(product, _):
    recipe = [copy.copy(ingredient) for ingredient in product.get("ingredients", [])]
    for ingredient_recipe in recipe:
        for ingredient in ingredients:
            if ingredient["id"] == ingredient_recipe["ingredient"]:
                ingredient_recipe["ingredient"] = ingredient
    return recipe


@ingredient_type.field("supplier")
def resolve_ingredient_suppliers(ingredient, _):
    if ingredient.get("supplier") is not None:
        for supplier in suppliers:
            if supplier["id"] == ingredient["supplier"]:
                return supplier


@ingredient_type.field("products")
def resolve_ingredient_products(ingredient, _):
    return [
        product
        for product in products
        if ingredient["id"] in product.get("ingredients", [])
    ]


@supplier_type.field("ingredients")
def resolve_supplier_ingredients(supplier, _):
    return [
        ingredient
        for ingredient in ingredients
        if supplier["id"] in ingredient.get("suppliers", [])
    ]

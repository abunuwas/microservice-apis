from ariadne import MutationType

from repository import ProductsRepository, IngredientsRepository, SuppliersRepository

mutation = MutationType()


@mutation.field('addSupplier')
def resolve_add_supplier(*_, name, input):
    input['name'] = name
    return SuppliersRepository().add(input)


@mutation.field('addIngredient')
def resolve_add_ingredient(*_, name, input):
    input['name'] = name
    return IngredientsRepository().add(input)


@mutation.field('addProduct')
def resolve_add_product(*_, name, type, input):
    repository = ProductsRepository()
    input['name'] = name
    return repository.add(product=input, product_type=type)


@mutation.field('updateProduct')
def resolve_update_product(*_, id, input):
    return ProductsRepository().update(id_=id, product_details=input)


@mutation.field('deleteProduct')
def resolve_delete_product(*_, id):
    ProductsRepository().delete(id)
    return True


@mutation.field('updateStock')
def resolve_update_stock(*_, id, changeAmount):
    ingredient = IngredientsRepository().get(id)
    ingredient['stock'] = changeAmount
    return ingredient

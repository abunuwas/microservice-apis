import uuid
from datetime import datetime
from itertools import islice

from exceptions import ItemNotFoundError

SUPPLIERS = [
    {
        'id': '92f2daae-a4f8-4aae-8d74-51dd74e5de6d',
        'name': 'Milk Supplier',
        'address': '77 Milk Way',
        'contactNumber': '0987654321',
        'email': 'milk@milksupplier.com',
    },
]

INGREDIENTS = [
    {
        'id': '602f2ab3-97bd-468e-a88b-bb9e00531fd0',
        'name': 'Milk',
        'stock': {
            'amount': 100.00,
            'unit': 'LITRES',
        },
        'supplier': '92f2daae-a4f8-4aae-8d74-51dd74e5de6d',
        'lastUpdated': datetime.now(),
    },
]


PRODUCTS = [
    {
        'id': '6961ca64-78f3-41d4-bc3b-a63550754bd8',
        'name': 'Walnut Bomb',
        'price': 37.00,
        'size': 'MEDIUM',
        'available': False,
        'ingredients': [
            {
                'ingredient': '602f2ab3-97bd-468e-a88b-bb9e00531fd0',
                'amount': 100.00,
                'unit': 'LITRES',
            }
        ],
        'hasFilling': False,
        'hasNutsToppingOption': True,
        'lastUpdated': datetime.now(),
    },
    {
        'id': 'e4e33d0b-1355-4735-9505-749e3fdf8a16',
        'name': 'Cappuccino Star',
        'price': 12.50,
        'size': 'SMALL',
        'available': True,
        'ingredients': [
            {
                'ingredient': '602f2ab3-97bd-468e-a88b-bb9e00531fd0',
                'amount': 100.00,
                'unit': 'LITRES',
            }
        ],
        'hasCreamOnTopOption': True,
        'hasServeOnIceOption': True,
        'lastUpdated': datetime.now(),
    },
]


class SuppliersRepository:
    @staticmethod
    def get(id_):
        for supplier in SUPPLIERS:
            if supplier['id'] == id_:
                return supplier
        raise ItemNotFoundError(f'Supplier with ID {id_} not found')

    @staticmethod
    def list():
        return SUPPLIERS

    @staticmethod
    def add(supplier):
        supplier['id'] = uuid.uuid4()
        SUPPLIERS.append(supplier)
        return supplier

    @staticmethod
    def update(id_, supplier_details):
        for supplier in SUPPLIERS:
            if supplier['id'] == id_:
                supplier.update(supplier_details)
                return supplier
        raise ItemNotFoundError(f'Supplier with ID {id_} not found')

    @staticmethod
    def delete(id_):
        for index, supplier in enumerate(SUPPLIERS):
            if supplier['id'] == id_:
                return SUPPLIERS.pop(index)
        raise ItemNotFoundError(f'Supplier with ID {id_} not found')


class IngredientsRepository:
    @staticmethod
    def get(id_):
        for ingredient in INGREDIENTS:
            if ingredient['id'] == id_:
                return ingredient
        raise ItemNotFoundError(f'Ingredient with ID {id_} not found')

    @staticmethod
    def list():
        return INGREDIENTS

    @staticmethod
    def add(ingredient):
        ingredient['id'] = uuid.uuid4()
        ingredient['lastUpdated'] = datetime.now()
        INGREDIENTS.append(ingredient)
        return ingredient

    @staticmethod
    def update(id_, ingredient_details):
        for ingredient in INGREDIENTS:
            if ingredient['id'] == id_:
                ingredient.update(ingredient_details)
                ingredient['lastUpdated'] = datetime.now()
                return ingredient
        raise ItemNotFoundError(f'Ingredient with ID {id_} not found')

    @staticmethod
    def delete(id_):
        for index, ingredient in enumerate(INGREDIENTS):
            if ingredient['id'] == id_:
                return INGREDIENTS.pop(index)
        raise ItemNotFoundError(f'Ingredient with ID {id_} not found')


class ProductsRepository:
    @staticmethod
    def get(id_):
        for product in PRODUCTS:
            if product['id'] == id_:
                return product
        raise ItemNotFoundError(f'Product with ID {id_} not found')

    @staticmethod
    def list():
        return PRODUCTS

    @staticmethod
    def _paginate(items, items_per_page, page):
        start = items_per_page * page
        end = start + items_per_page
        return [item for item in islice(items, start, end)]

    def filter(self, filters):
        if filters is None:
            return PRODUCTS
        filtered = [
            product for product in PRODUCTS
            if product['available'] is filters['available']
        ]
        if filters.get('minPrice') is not None:
            filtered = [
                product for product in PRODUCTS
                if product['price'] >= filters['minPrice']
            ]
        if filters.get('maxPrice') is not None:
            filtered = [
                product for product in PRODUCTS
                if product['price'] <= filters['maxPrice']
            ]
        filtered.sort(
            key=lambda product: product[filters['sortBy']],
            reverse=filters['sort'] == 'DESCENDING'
        )
        return self._paginate(
            filtered, filters['resultsPerPage'], filters['page']
        )

    @staticmethod
    def add(product, product_type):
        product.update({
            'id': uuid.uuid4(),
            'available': product.get('available', False),
            'ingredients': product.get('ingredients', []),
            'lastUpdated': datetime.now(),
        })
        if product_type == 'cake':
            product.update({
                'hasFilling': product['hasFilling'],
                'hasNutsToppingOption': product['hasNutsToppingOption'],
            })
        else:
            product.update({
                'hasCreamOnTopOption': product['hasCreamOnTopOption'],
                'hasServeOnIceOption': product['hasServeOnIceOption'],
            })
        PRODUCTS.append(product)
        return product

    @staticmethod
    def update(id_, product_details):
        for product in PRODUCTS:
            if product['id'] == id_:
                product.update(product_details)
                product['lastUpdated'] = datetime.now()
                return product
        raise ItemNotFoundError(f'Product with ID {id_} not found')

    @staticmethod
    def delete(id_):
        for index, product in enumerate(PRODUCTS):
            if product['id'] == id_:
                PRODUCTS.pop(index)
                return
        raise ItemNotFoundError(f'Product with ID {id_} not found')

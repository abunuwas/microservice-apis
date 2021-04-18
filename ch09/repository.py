_INGREDIENTS = [
    {
        'id': 'qwer',
        'name': 'Milk',
        'stock': 100.0
    }
]


_CAKES = [
    {
        'id': 'asdf',
        'name': 'Capuccino',
        'price': 10.0,
        'ingredients': ['qwer'],
        'has_filling': False,
        'has_nuts_topping_option': True,
    }
]

_BEVERAGES = [
    {
        'id': 'asdf',
        'name': 'Capuccino',
        'price': 10.0,
        'ingredients': ['qwer'],
        'has_cream_on_top_option': False,
        'has_serve_on_ice_option': True,
    }
]


class IngredientsRepository:
    def get(self):
        pass

    def list(self):
        pass

    def add(self):
        pass

    def update(self):
        pass


class ProductsRepository:
    def get(self):
        pass

    def list(self):
        pass

    def add(self):
        pass

    def update(self):
        pass

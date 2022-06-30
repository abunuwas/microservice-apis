from datetime import datetime


suppliers = [
    {
        'id': '92f2daae-a4f8-4aae-8d74-51dd74e5de6d',
        'name': 'Milk Supplier',
        'address': '77 Milk Way',
        'contactNumber': '0987654321',
        'email': 'milk@milksupplier.com',
    },
]

ingredients = [
    {
        'id': '602f2ab3-97bd-468e-a88b-bb9e00531fd0',
        'name': 'Milk',
        'stock': {
            'quantity': 100.00,
            'unit': 'LITERS',
        },
        'products': [],
        'supplier': '92f2daae-a4f8-4aae-8d74-51dd74e5de6d',
        'lastUpdated': datetime.utcnow(),
    },
]


products = [
    {
        'id': '6961ca64-78f3-41d4-bc3b-a63550754bd8',
        'name': 'Walnut Bomb',
        'price': 37.00,
        'size': 'MEDIUM',
        'available': False,
        'ingredients': [
            {
                'ingredient': '602f2ab3-97bd-468e-a88b-bb9e00531fd0',
                'quantity': 100.00,
                'unit': 'LITERS',
            }
        ],
        'hasFilling': False,
        'hasNutsToppingOption': True,
        'lastUpdated': datetime.utcnow(),
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
                'quantity': 100.00,
                'unit': 'LITERS',
            }
        ],
        'hasCreamOnTopOption': True,
        'hasServeOnIceOption': True,
        'lastUpdated': datetime.utcnow(),
    },
]

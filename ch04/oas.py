from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

specification = APISpec(
    title='Orders API',
    version='1.0.0',
    openapi_version='3.0.3',
    plugins=[MarshmallowPlugin()],
    **{
        'info': {
            'description': 'API that allows you to manage orders for CoffeeMesh'
        },
        'servers': [
            {
                'url': 'https://coffeemesh.com',
                'description': 'main production server'
            },
            {
                'url': 'https://coffeemesh-staging.com',
                'description': 'staging server for testing purposes only'
            }
        ]
    }
)

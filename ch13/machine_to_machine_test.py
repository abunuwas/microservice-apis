import requests


def get_access_token():
    payload = {
        "client_id": "MQjOO2o3rdM3XhoiTB5cr497Irr63g8n",
        "client_secret": "gU5CsCxcFQT3RnJXupaMPsg6-PwzPiwo1Q0K0Pg16fLkWG1AdgXjGasZoYNkP2_j",
        "audience": "http://127.0.0.1:8000/orders",
        "grant_type": "client_credentials"
    }

    response = requests.post(
        "https://coffeemesh-dev.eu.auth0.com/oauth/token",
        json=payload,
        headers={'content-type': "application/json"}
    )

    return response.json()['access_token']


def create_order(token):
    order_payload = {
        'order': [{
            'product': 'asdf',
            'size': 'small',
            'quantity': 1
        }]
    }

    order = requests.post(
        'http://127.0.0.1:8000/orders',
        json=order_payload,
        headers={'content-type': "application/json", "Authorization": f"Bearer {token}"}
    )

    return order.json()


access_token = get_access_token()
print(access_token)
order = create_order(access_token)
print(order)

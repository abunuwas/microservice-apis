import json
import dredd_hooks
import requests

response_stash = {}


@dredd_hooks.after('/orders > Creates an order > 201 > application/json')
def save_created_task(transaction):
    response_payload = transaction['real']['body']
    task_id = json.loads(response_payload)['id']
    response_stash['created_task_id'] = task_id


@dredd_hooks.before('/orders/{orderId} > Returns the details of a specific order > 200 > application/json')
def before_get_task(transaction):
    transaction['fullPath'] = '/orders/' + response_stash['created_task_id']
    transaction['request']['uri'] = '/orders/' + response_stash['created_task_id']


@dredd_hooks.before('/orders/{orderId} > Replaces an existing order > 200 > application/json')
def before_put_task(transaction):
    transaction['fullPath'] = '/orders/' + response_stash['created_task_id']
    transaction['request']['uri'] = '/orders/' + response_stash['created_task_id']


@dredd_hooks.before('/orders/{orderId} > Deletes an existing order > 204')
def before_delete_task(transaction):
    transaction['fullPath'] = '/orders/' + response_stash['created_task_id']
    transaction['request']['uri'] = '/orders/' + response_stash['created_task_id']


@dredd_hooks.before('/orders/{orderId}/pay > Processes payment for an order > 200 > application/json')
def before_pay_task(transaction):
    response = requests.post('http://127.0.0.1:8000/orders', json={'order': [{'product': 'string', 'size': 'small', 'quantity': 1}]})
    id_ = response.json()['id']
    transaction['fullPath'] = '/orders/' + id_ + '/pay'
    transaction['request']['uri'] = '/orders/' + id_ + '/pay'


@dredd_hooks.before('/orders/{orderId}/cancel > Cancels an order > 200 > application/json')
def before_cancel_task(transaction):
    response = requests.post('http://127.0.0.1:8000/orders', json={'order': [{'product': 'string', 'size': 'small', 'quantity': 1}]})
    id_ = response.json()['id']
    transaction['fullPath'] = '/orders/' + id_ + '/cancel'
    transaction['request']['uri'] = '/orders/' + id_ + '/cancel'

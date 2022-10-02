import logging

import json
import dredd_hooks
import requests

response_stash = {}


@dredd_hooks.after("/orders > Creates an order > 201 > application/json")
def save_created_order(transaction):
    logger = logging.getLogger()
    logger.error(transaction)
    response_payload = transaction["real"]["body"]
    task_id = json.loads(response_payload)["id"]
    response_stash["created_order_id"] = task_id


@dredd_hooks.before(
    "/orders/{order_id} > Returns the details of a specific order > 200 > "
    "application/json"
)
def before_get_order(transaction):
    transaction["fullPath"] = "/orders/" + response_stash["created_order_id"]
    transaction["request"]["uri"] = "/orders/" + response_stash["created_order_id"]


order_item_strategy = st.fixed_dictionaries(
    {
        "product": values_strategy,
        "size": st.one_of(st.sampled_from(("small", "medium", "big")))
        | values_strategy,
        "quantity": values_strategy,
    }
)


@dredd_hooks.before(
    "/orders/{order_id} > Replaces an existing order > 200 > " "application/json"
)
def before_put_order(transaction):
    transaction["fullPath"] = "/orders/" + response_stash["created_order_id"]
    transaction["request"]["uri"] = "/orders/" + response_stash["created_order_id"]


@dredd_hooks.before("/orders/{order_id} > Deletes an existing order > 204")
def before_delete_order(transaction):
    transaction["fullPath"] = "/orders/" + response_stash["created_order_id"]
    transaction["request"]["uri"] = "/orders/" + response_stash["created_order_id"]


@dredd_hooks.before(
    "/orders/{order_id}/pay > Processes payment for an order > 200 > "
    "application/json"
)
def before_pay_order(transaction):
    response = requests.post(
        "http://127.0.0.1:8000/orders",
        json={"order": [{"product": "string", "size": "small", "quantity": 1}]},
    )
    id_ = response.json()["id"]
    transaction["fullPath"] = "/orders/" + id_ + "/pay"
    transaction["request"]["uri"] = "/orders/" + id_ + "/pay"


@dredd_hooks.before(
    "/orders/{order_id}/cancel > Cancels an order > 200 > application/json"
)
def before_cancel_order(transaction):
    response = requests.post(
        "http://127.0.0.1:8000/orders",
        json={"order": [{"product": "string", "size": "small", "quantity": 1}]},
    )
    id_ = response.json()["id"]
    transaction["fullPath"] = "/orders/" + id_ + "/cancel"
    transaction["request"]["uri"] = "/orders/" + id_ + "/cancel"


@dredd_hooks.before("/orders > Creates an order > 422 > application/json")
def fail_create_order(transaction):
    transaction["request"]["body"] = json.dumps(
        {"order": [{"product": "string", "size": "asdf"}]}
    )


@dredd_hooks.before(
    "/orders/{order_id} > Returns the details of a specific order > 422 > "
    "application/json"
)
@dredd_hooks.before(
    "/orders/{order_id}/cancel > Cancels an order > 422 > application/json"
)
@dredd_hooks.before(
    "/orders/{order_id}/pay > Processes payment for an order > 422 > "
    "application/json"
)
@dredd_hooks.before(
    "/orders/{order_id} > Replaces an existing order > 422 > " "application/json"
)
@dredd_hooks.before(
    "/orders/{order_id} > Deletes an existing order > 422 > " "application/json"
)
def fail_target_specific_order(transaction):
    transaction["fullPath"] = transaction["fullPath"].replace(
        "d222e7a3-6afb-463a-9709-38eb70cc670d", "8"
    )
    transaction["request"]["uri"] = transaction["request"]["uri"].replace(
        "d222e7a3-6afb-463a-9709-38eb70cc670d", "8"
    )

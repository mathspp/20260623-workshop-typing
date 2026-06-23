"""
This code doesn't run but passes type checking.
Don't fix the bugs in the code yet.
Use a typed dict to improve the safety of this code and then use a type checker to find the errors.
"""

checkout_1 = {
    "currency": "EUR",
    "price": 34.99,
    "items": 3,
    "discount_code": "PYTHON10",
}

checkout_2 = {
    "currency": "USD",
    "price": 19.50,
    "items": 1,
    "discount": None,
}

checkout_3 = {
    "currency": "USD",
    "price": 120.00,
    "item": 5,
    "discount_code": "SUMMER",
}


def process_checkout(checkout: dict) -> str:
    currency = checkout["currency"]
    price = checkout["price"]
    items = checkout["items"]
    discount_code = checkout["discount_code"]

    if discount_code is None:
        discount_message = "No discount was used."
    else:
        discount_message = f"Discount code {discount_code!r} was used."

    return (
        f"Processed checkout for {items} item(s): "
        f"{price:.2f} {currency}. "
        f"{discount_message}."
    )


checkouts = [checkout_1, checkout_2, checkout_3]

for checkout in checkouts:
    print(process_checkout(checkout))

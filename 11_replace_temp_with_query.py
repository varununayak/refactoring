# Replace Temp with Query

class Order:

    def __init__(self, quantity: int, item_price: float) -> None:
        self.quantity = quantity
        self.item_price = item_price


def get_price(order: Order) -> float:
    base_price = order.quantity * order.item_price
    if base_price > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return base_price * discount_factor


"""
Temporary variables are used to capture the value of some code to refer to it later in a function.
Using a temp allows us to refer to the value while explaining its meaning (through the name) and
avoiding repetition of the code that calculates it.

Putting this logic into a function sets up a strong boundary between logic and original function
and helps spot awkward dependencies and side effects.

We must make sure that the logic used to calculate the variable yields the same result every time.
"""


class OrderBetter:

    def __init__(self, quantity: int, item_price: float) -> None:
        self.quantity = quantity
        self.item_price = item_price

    @property
    def base_price(self) -> float:
        return self.quantity * self.item_price

    @property
    def discount_factor(self) -> float:
        return 0.95 if self.base_price > 1000 else 0.98


def get_price_refactored(order: OrderBetter) -> float:
    return order.base_price * order.discount_factor


if __name__ == "__main__":
    print(f"Price: {get_price(Order(200, 10))}")
    print(f"Price: {get_price_refactored(OrderBetter(200, 10))}")

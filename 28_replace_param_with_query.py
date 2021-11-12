# Replace Parameter with Query

class Order:

    def __init__(self, quantity: int, item_price: float) -> None:
        self.quantity = quantity
        self.item_price = item_price

    @property
    def final_price(self) -> float:
        base_price = self.quantity * self.item_price
        discount_level = 2 if self.quantity > 100 else 1
        return self._discounted_price(base_price, discount_level)

    def _discounted_price(self, base_price: float, discount_level: int) -> float:
        return base_price * 0.95 if discount_level == 1 else base_price * 0.9


"""
 The parameter list should concisely summarize the points of variability 
 of that function. It is easier to understand if the parameter list is short.

 If a call passes a value that a function can easily determine for itself,
 that's a form of duplication. The objective is to simplify life for callers.
 The safest case for replace parameter with query is when the value of the parameter
 that is removed is obtained simply by querying another parameter in the parameter list.
"""


class OrderBetter:

    def __init__(self, quantity: int, item_price: float) -> None:
        self.quantity = quantity
        self.item_price = item_price

    @property
    def final_price(self) -> float:
        base_price = self.quantity * self.item_price
        return self._discounted_price(base_price)

    def _discounted_price(self, base_price: float) -> float:
        discount_level = 2 if self.quantity > 100 else 1
        return base_price * 0.95 if discount_level == 1 else base_price * 0.9


if __name__ == "__main__":
    order = Order(10, 25.99)
    print(f"Final Price: ${order.final_price : .2f}")
    order = OrderBetter(10, 25.99)
    print(f"Final Price: ${order.final_price : .2f}")
